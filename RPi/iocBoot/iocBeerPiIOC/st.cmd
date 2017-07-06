#!../../bin/linux-arm/BeerPiIOC

## You may have to change BeerPiIOC to something else
## everywhere it appears in this file

< envPaths

epicsEnvSet(STREAM_PROTOCOL_PATH,"/home/pi/EPICS/BeerPi/BeerPiIOCApp/Db/")
#epicsEnvSet(STREAM_PROTOCOL_PATH,"BeerPiIOCApp/Db")


#epicsEnvSet(STREAM_PROTOCOL_PATH,".:../protocols")


cd "/home/pi/EPICS/BeerPi"

## Register all support components
dbLoadDatabase "dbd/BeerPiIOC.dbd"
BeerPiIOC_registerRecordDeviceDriver pdbbase


drvAsynSerialPortConfigure("SERIALPORT","/dev/ttyACM0",0,0,0)
#drvAsynSerialPortConfigure("SERIALPORT","/dev/ttyACM1",0,0,0)
asynSetOption("SERIALPORT",-1,"baud","115200")
asynSetOption("SERIALPORT",-1,"bits","8")
asynSetOption("SERIALPORT",-1,"parity","none")
asynSetOption("SERIALPORT",-1,"stop","1")
asynSetOption("SERIALPORT",-1,"clocal","Y")
asynSetOption("SERIALPORT",-1,"crtscts","N")

## Load record instances
dbLoadRecords("db/brew.db","user=BeerPi,PORT='SERIALPORT'")

cd "/home/pi/EPICS/BeerPi/iocBoot/iocBeerPiIOC"
iocInit

## Start any sequence programs
#seq sncxxx,"user=BeerPi"
