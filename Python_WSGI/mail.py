import smtplib
import time
import epics

server=smtplib.SMTP('smtp.gmail.com',587)

record = 0

i = 0

while True:
    send = 0
    if epics.caget('BeerPi:Tbeer') == None:
        send = 1
        msg = "Failed to connect to BeerPi!"
    elif epics.caget('BeerPi:Tbeer.SEVR') != 0:
        send = 2
        msg = "There is something wrong with the PV BeerPi:Tbeer. Please check it's SEVR field."
    else:
        Tbeer  = epics.caget('BeerPi:Tbeer')
        Tref = epics.caget('BeerPi:Tref')
        Tbeer_min = Tref  - 1.5
        Tbeer_max = Tref  + 1.5

    if Tbeer>Tbeer_max and send == 0:
        send = 3
        msg = "Beer temperature is too high! Current value: %f DegC is %f DegC above the reference value. " %(Tbeer,Tbeer-Tref)

    if Tbeer<Tbeer_min and send == 0:
        send = 4
        msg = "Beer temperature is too low! Current value: %f DegC is %f DegC below the reference value. " %(Tbeer,Tref-Tbeer)

    if send == 0:
        print "OK. Tbeer = %f" %Tbeer

    if i>180:
        record = 0

    if record == send:
        send = 0
        i+=1

    if send != 0:
        i = 0
        record = send
        try:
            server.ehlo()
            server.starttls()
            server.ehlo
            server.login("cervejasnucleares2017@gmail.com","fermentacao2017")
            server.sendmail("cervejasnucleares2017@gmail.com","bernardo.brotas@gmail.com", msg)
        except:
            print "Falha no Envio"

    time.sleep(60)
