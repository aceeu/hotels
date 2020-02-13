#!/usr/bin/env python3
import cgi
import os
from os import environ
from session import checkLogin, newSession

#path = os.path.dirname(os.path.abspath(__file__))

form = cgi.FieldStorage()
formname = form.getfirst("name", '')
formpass = form.getfirst("pass", '')


print ("Content-type: text/html")
# print ("<title>Hello</title>")
# print("<p>{}<p>".format(environ['HTTP_COOKIE']))
key, pdict = cgi.parse_header(environ['HTTP_COOKIE'])
# print("<p>{}<p>".format(pdict['sid']))

logged = checkLogin(formname, formpass)
uuid = ''
if logged:
    uuid = newSession(formname)

print("Set-cookie: sid={};HttpOnly".format(uuid))
print("")


if logged:
    print ("<p>Вы в системе {}</p>".format(formname))
else:
    print('<p>Вы не авторизированы</p>')

