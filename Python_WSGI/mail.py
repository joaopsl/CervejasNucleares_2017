
import smtplib
import time
import epics

server=smtplib.SMTP('smtp.gmail.com',587)

while True:
    send = 0
    Tbeer  = epics.caget('BeerPi:Tbeer')
    Tref = epics.caget('BeerPi:Tref')
    Tbeer_min = Tref - 1.5
    Tbeer_max = Tref + 1.5
    if Tbeer>Tbeer_max:
        send = 1
        msg = "ALARM: Beer temperature is too high! Current value: %f DegC is %f DegC above the reference value. " %(Tbeer,Tbeer-Tref)
    if Tbeer<Tbeer_min:
        send = 1
        msg = "ALARM: Beer temperature is too low! Current value: %f DegC is %f DegC below the reference value. " %(Tbeer,Tref-Tbeer)
    if send == 1:
        try:
            server.ehlo()
            server.starttls()
            server.ehlo
            server.login("cervejasnucleares2017@gmail.com","fermentacao2017")
            server.sendmail("cervejasnucleares2017@gmail.com","henriquegs96@hotmail.com", msg)
            print "Mail enviado"
        except:
            print "Falha no Envio"
    print '%f DegC' %Tbeer
    time.sleep(60)
