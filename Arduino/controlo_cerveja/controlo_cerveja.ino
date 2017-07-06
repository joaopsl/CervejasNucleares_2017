#include <OneWire.h>
#include <DallasTemperature.h>

// Data wire is plugged into port 10 on the Arduino
#define ONE_WIRE_BUS 10

// Temperature precision is 12 bits (max.)
#define TEMPERATURE_PRECISION 12

// Rele is plugged into port 8 on the Arduino
#define RELE 8

// Temperature is measured every 1000 milliseconds
#define TEMP_INTERVAL 1000

// Duty cycle is 60 minutes
// #define DUTY_CYCLE 3600000

#define DUTY_CYCLE 1800000

// Rele is on for 5 seconds every 60 minutes by default
#define DEFAULT_ON_TIME 300000

// Setup a OneWire instance to communicate with any OneWire devices
OneWire oneWire(ONE_WIRE_BUS);

// Pass the oneWire reference to Dallas Temperature
DallasTemperature sensors(&oneWire);

DeviceAddress tempDeviceAddress; // Stores a found device address

int numberOfDevices; // Number of temperature devices found
String input = ""; // String to store the requests from the serial
int numero; // Index number of the intended temperature device
// Temperature values
float temperatura0;
float temperatura1;
float temperatura2;

bool RELE_state = 0; // Rele state
unsigned long prevTime; // Last time the temperature was updated
unsigned long prevTime2; // Last time the rele was updated
unsigned long onTime = DEFAULT_ON_TIME;
unsigned long onTime_next = 300000;

void setup (void) {
  // Start serial port
  Serial.begin(115200);

  // Start up the library
  sensors.begin();

  // Grab a count of devices on the wire
  numberOfDevices = sensors.getDeviceCount();

  // Loop through each device
  for (int i = 0; i < numberOfDevices; i++) {
    // Search the wire for address
    if (sensors.getAddress(tempDeviceAddress, i)) {
      // Set the resolution
      sensors.setResolution(tempDeviceAddress, TEMPERATURE_PRECISION);
    }
  }

  // Define rele pin as OUTPUT and set it turned off by default
  pinMode(RELE, OUTPUT);
  digitalWrite(RELE, LOW);

  pinMode(LED_BUILTIN, OUTPUT);
}

void serial_protocol() {
  while (Serial.available() > 0) {
    char lastRecvd = Serial.read();

    // if end of message has arrived
    if (lastRecvd == '\n') {
      switch (input[0]) {
        // Request for temperature readout
        case 'T':
            Serial.print("T1=");
            Serial.print(temperatura0);
            Serial.print(", ");
            Serial.print("T2=");
            Serial.print(temperatura1);
            Serial.print(", ");
            Serial.print("T3=");
            Serial.print(temperatura2);
            Serial.print(", ");
            Serial.print("S=");
            Serial.print(String(RELE_state));
            Serial.print("\r\n");
            input="";
            break;

         // Request to turn the rele off
        case 'L':
          RELE_state = 0;
          input="";
          break;

        // Request to turn the rele on
        case 'H':
          RELE_state = 1;
          input="";
          break;

        // Request for the rele state
        case 'S':
          Serial.print("S=");
          Serial.print(String(RELE_state));
          Serial.print("\r\n");
          input = "";
          break;

        case 'D':
          input = input.substring(2); // Format is D=___

          // if new duty cycle is less than 1 hour
          if (input.toInt() < DUTY_CYCLE / 1000) {
            onTime_next = input.toInt();
            onTime_next = onTime_next * 1000; // Convert to milliseconds
          }
          
          input = "";
          break;
          
        default:
          input = "";
          break;
      }
    } else {
      input += lastRecvd;
    }
  }
}

void loop (void) {
  unsigned long currentTime = millis();
  
  serial_protocol();

  // Call sensors.requestTemperatures() to issue a global temperature
  // Request to all devices on the bus
  sensors.requestTemperatures(); // Send the command to get temperatures

  // If current time minus previous time exceeds TEMP_INTERVAL
  if (currentTime - prevTime > TEMP_INTERVAL) {
    prevTime = currentTime;

    // Update temperatures
    temperatura0 = sensors.getTempCByIndex(0);
    temperatura1 = sensors.getTempCByIndex(1);
    temperatura2 = sensors.getTempCByIndex(2);
  }

  // Control of rele
  // onTime defines for how much time of one hour it is on
  if (currentTime - prevTime2 > onTime) {

    if (RELE_state == 1) {
//      Serial.print("desliguei ");
//      Serial.print(currentTime/1000);
//      Serial.print("\r\n");
      digitalWrite(LED_BUILTIN, LOW);
      digitalWrite(RELE, LOW);
      RELE_state = 0;
    }

    // If DUTY_CYCLE has passed, update onTime for the next hour
    if (currentTime - prevTime2 > DUTY_CYCLE) {
      prevTime2 = currentTime;
      onTime = onTime_next;
    }
    
  } else {
    
    if (RELE_state == 0) {
//      Serial.print("liguei ");
//      Serial.print(currentTime/1000);
//      Serial.print("\r\n");
      digitalWrite(LED_BUILTIN, HIGH);
      RELE_state = 1;
      digitalWrite(RELE, HIGH);
    }
  }
}

