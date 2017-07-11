import epics

#from time import *

def application(environ,start_response):
    value  = epics.caget('BeerPi:Tbeer')
    value2 = epics.caget('BeerPi:Tfrigo')
    value3 = epics.caget('BeerPi:Text')
    #now = ctime()

    status = '200 OK'
    html = '<html>\n' \
	   '<head>' \
           '<title>IST Beer Pi</title>' \
           '<meta http-equiv="refresh" content="10" />' \
    	   '</head>\n' \
           '<body>\n' \
           '<div style="width: 100%; font-size: 40px; font-weight: bold; text-align: center;">\n' \
           'BeerPi Project Real-time Temperatures:\n' \
           '<div style="width: 100%; font-size: 30px; font-weight: bold; text-align: center;">\n' \
           'Beer: ' + str(value)+ ' Deg\n' \   
	   '<div style="width: 100%; font-size: 30px; font-weight: bold; text-align: center;">\n' \
           'Fridge: ' + str(value2)+ ' Deg\n' \		
	   '<div style="width: 100%; font-size: 30px; font-weight: bold; text-align: center;">\n' \
           'Outside: ' + str(value3)+ ' Deg\n' \
           '</div>\n' \
           '</body>\n' \
           '</html>\n'
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    return [html]


