import smtplib
import sleep
import epics

server=smtplib.SMTP('smtp.gmail.com',587)

while(1)
    Tbeer  = epics.caget('BeerPi:Tbeer')
    Tref = epics.caget('BeerPi:Tref')
    Tbeer_min = Tref - 1.5
    Tbeer_max = Tref + 1.5
    if Tbeer>Tbeer_max or Tbeer<Tbeer_min:
        try:
            server.ehlo()
            server.starttls()
            server.ehlo
            server.login("cervejasnucleares2017@gmail.com","fermentacao2017")
            msg = "Hello!"
            server.sendmail("cervejasnucleares2017@gmail.com","henriquegs96@hotmail.com", msg)
            print "Mail enviado"
        except:
            print "Falha no Envio"
    print Tbeer + 'DegC'
    sleep(30)
