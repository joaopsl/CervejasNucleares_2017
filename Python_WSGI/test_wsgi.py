import epics

import time

def application(environ,start_response):
    value  = epics.caget('BeerPi:Tbeer')
    value2 = epics.caget('BeerPi:Tfrigo')
    value3 = epics.caget('BeerPi:Text')
    now = time.ctime()
    #data_uri = open('/home/pi/BeerGit/CervejasNucleares_2017/Python_WSGI/group_photo.jpg', 'rb').read().encode('base64').replace('\n', '')
    #img_tag = '<img src="data:image/png;base64,{0}"  alt="Group Photo">'.format(data_uri)
    status = '200 OK'
    html = '<html>\n' \
	   '<head>' \
           '<title>IST Beer Pi</title>' \
           '<meta http-equiv="refresh" content="10" />' \
    	   '</head>\n' \
           '<body>\n' \
           '<div style="width: 100%; font-size: 40px; font-weight: bold; text-align: center;">\n' \
           'BeerPi Project in Real-Time:\n' \
           '</div>\n' \
           '<div style="width: 100%; font-size: 30px; font-weight: bold; text-align: center;">\n' \
           'Beer Temperature: ' + str(value)+ ' Deg\n' \
	   '<div style="width: 100%; font-size: 30px; font-weight: bold; text-align: center;">\n' \
           'Fridge Temperature: ' + str(value2)+ ' Deg\n' \
	   '<div style="width: 100%; font-size: 30px; font-weight: bold; text-align: center;">\n' \
           'Outside Temperature: ' + str(value3)+ ' Deg\n' \
	   '<div style="width: 100%; font-size: 30px; font-weight: bold; text-align: center;">\n' \
            'Current Time: ' +now+ '\n' \
           '</div>\n' \
           '</body>\n' \
           '</html>\n'
    response_header = [('Content-type','text/html')]
    start_response(status,response_header)
    return [html]
