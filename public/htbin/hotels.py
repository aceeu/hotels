import cgi
import os
import uuid
import json
from os import environ
from files import removeRecord, existRecord, addRecord

path = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(path, 'hotels.dat')
method = environ['REQUEST_METHOD'].upper() #POST

print ("Content-type: text/html")
print("")
# print('hotels.py handler {}'.format(method))
if (method == 'POST'):
    form = cgi.FieldStorage()
    number = form.getfirst("number", '')
    floors = form.getfirst("floors", '')
    count = form.getfirst("count", '')
    country = form.getfirst("country", '')
    city = form.getfirst("city", '')
    street = form.getfirst("street", '')
    house = form.getfirst("house", '')

    res = addRecord(filename, (number, floors, count, country, city, street, house))
print("""<html><head>
        <meta http-equiv="Refresh" content="0; url=../index.html" />
        </head>
        </html>""")