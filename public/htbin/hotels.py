import cgi
import os
import uuid
import json
from os import environ
from files import removeRecord, existRecord, addRecord, listRecords
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
        removeRecord(hotelsfilename, lambda line: line.split(',')[0] == uuid)
        redirectTo('./hotels.py') #list of hotels
    else:
        number = form.getfirst("number", '')
        floors = form.getfirst("floors", '')
        count = form.getfirst("count", '')
        country = form.getfirst("country", '')
        city = form.getfirst("city", '')
        street = form.getfirst("street", '')
        house = form.getfirst("house", '')
        res = addRecord(hotelsfilename, (number, floors, count, country, city, street, house))
        redirectTo('../index.html')
elif (method == "GET"):
    filename = os.path.join(path, 'hotels.templ')
    with open(filename, 'r') as f:
        html = f.read()
        template = Template(html)
        listr = listRecords(hotelsfilename)
        print(template.render(hotels_list=listr))

    # listr = listRecords(filename)
    # li = ''
    # for row in listr:
    #     li += '<li>'
    #     li += row
    #     li += '</li>'
    #     print("""

    #     """.format(li))