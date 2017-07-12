import smtplib
import sleep
import epics

server=smtplib.SMTP('smtp.gmail.com',587)

Tbeer_min = 17.5
Tbeer_max = 19.5

while(1)
    Tbeer  = epics.caget('BeerPi:Tbeer')
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
