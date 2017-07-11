import epics

#from time import *

 def application(environ,start_response):
      value  = epics.caget('BeerPi:Tbeer')
     value2 = epics.caget('BeerPi:Tfrigo')
     value3 = epics.caget('BeerPi:Text')
      status = '200 OK'
      html = '<html>\n' \
  	   '<head>' \
           '</div>\n' \
           '<div style="width: 100%; font-size: 30px; font-weight: bold; text-align: center;">\n' \
           'Beer Temperature: ' + str(value)+ ' Deg\n' \
 	   '<div style="width: 100%; font-size: 30px; font-weight: bold; text-align: center;">\n' \
           'Fridge Temperature: ' + str(value2)+ ' Deg\n' \
 	   '<div style="width: 100%; font-size: 30px; font-weight: bold; text-align: center;">\n' \
           'Outside Temperature: ' + str(value3)+ ' Deg\n' \
           '</div>\n' \
           '</body>\n' \
           '</html>\n'
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    return [html]

