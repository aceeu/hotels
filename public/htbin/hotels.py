import cgi
import os
import uuid
import json
from os import environ
# from files import removeRecord, existRecord, addRecord, listRecords
from db import addHotel, removeHotel, listHotels, listHotelsWithoutAdmin
from jinja2 import Template
from common import redirectTo

path = os.path.dirname(os.path.abspath(__file__))
hotelsfilename = os.path.join(path, 'hotels.dat')
method = environ['REQUEST_METHOD'].upper() #POST


#print (environ)

if method == 'POST':
    print ("Content-type: text/html")
    print ("")
    form = cgi.FieldStorage()
    uuid = form.getfirst('uuid')
    if uuid is not None:
        removeHotel(uuid)
        redirectTo('./hotels.py') #list of hotels
    else:
        print ("Content-type: text/html")
        print ("")
        name = form.getfirst("name", '')
        floors = form.getfirst("floors", '')
        count = form.getfirst("count", '')
        country = form.getfirst("country", '')
        city = form.getfirst("city", '')
        street = form.getfirst("street", '')
        house = form.getfirst("house", '')
        addHotel(name, floors, count, country, city, street, house)
        redirectTo('../index.html')
elif (method == "GET"):
    if environ['QUERY_STRING'] == 'addadmin':
        print ("Content-type: application/json")
        print ("")
        listr = listHotelsWithoutAdmin()
        #res = dict(name=name, usertype=usertype)
        print(json.dumps(listr))

    else:
        print ("Content-type: text/html")
        print ("")
        filename = os.path.join(path, 'list.templ')
        with open(filename, 'r') as f:
            html = f.read()
            template = Template(html)
            listr = listHotels() #[(id, name, country, city, street)]
            
            print(template.render(list=listr, action='./hotels.py', title='Hotels list'))
