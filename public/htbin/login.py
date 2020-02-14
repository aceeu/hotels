#!/usr/bin/env python3
import cgi
import os
from os import environ
from session import checkLogin, newSession

#path = os.path.dirname(os.path.abspath(__file__))

form = cgi.FieldStorage()
formname = form.getfirst("name", '')
formpass = form.getfirst("pass", '')

key, pdict = cgi.parse_header(environ['HTTP_COOKIE'])
uuid = ''
logged, usertype = checkLogin(formname, formpass)
if logged:
    uuid = newSession(formname, usertype)
print ("Content-type: text/html")
print("Set-cookie: sid={};HttpOnly".format(uuid))
print('')
if (logged):
    print("""<html><head>
        <meta http-equiv="Refresh" content="0; url=../index.html" />
        </head>
        <body>
        </body>
        </html>""")
else: print("""<html><head>
        <meta http-equiv="Refresh" content="0; url=../login.html" />
        </head>
        <body>
        </body>
        </html>""")


# if logged:
#     print ("<p>Вы в системе {}</p>".format(formname))
# else:
#     print('<p>Вы не авторизированы</p>')

