import cgi
import os
import uuid
import json
from os import environ
# from files import removeRecord, existRecord, addRecord, listRecords
from db import addHotel, removeHotel, listHotels
from jinja2 import Template
from common import redirectTo

path = os.path.dirname(os.path.abspath(__file__))
hotelsfilename = os.path.join(path, 'hotels.dat')
method = environ['REQUEST_METHOD'].upper() #POST


print ("Content-type: text/html")
print ("")
if method == 'POST':
    form = cgi.FieldStorage()
    uuid = form.getfirst('uuid')
    if uuid is not None:
        removeHotel(uuid)
        redirectTo('./hotels.py') #list of hotels
    else:
        floors = form.getfirst("floors", '')
        count = form.getfirst("count", '')
        country = form.getfirst("country", '')
        city = form.getfirst("city", '')
        street = form.getfirst("street", '')
        house = form.getfirst("house", '')
        addHotel(floors, count, country, city, street, house)
        redirectTo('../index.html')
elif (method == "GET"):
    filename = os.path.join(path, 'list.templ')
    with open(filename, 'r') as f:
        html = f.read()
        template = Template(html)
        listr = listHotels()
        print(template.render(list=listr, action='./hotels.py', title='Hotels list'))
