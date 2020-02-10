#!/usr/bin/env python3
import cgi
import os

path = os.path.dirname(os.path.abspath(__file__))

form = cgi.FieldStorage()
name = form.getfirst("name", '')
p = form.getfirst("pass", '')

print ("Content-type: text/html")

print()

filename = os.path.join(path, 'users.dat');
with open(filename) as f_obj: lines = f_obj.readlines()
for line in lines:
    items = line.split(',')
    print('<p>')
    for itm in items:
        print('<span>{}</span>'.format(itm.rstrip()))
    print('</p>')

print ("<title>Hello</title>")
print ("<p>{}<p>".format(name))
print ("<p>{}<p>".format(p))
