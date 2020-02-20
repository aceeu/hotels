import cgi
import os
import uuid
from os import environ
from db import addUser, listUsers, removeUser
from common import redirectTo
from session import isSession
from jinja2 import Template
path = os.path.dirname(os.path.abspath(__file__))
method = environ['REQUEST_METHOD'].upper() #POST

print ("Content-type: text/html")
print ("")
key, pdict = cgi.parse_header('ddd=sss; ' + environ['HTTP_COOKIE'])
# print("<p>{}<p>".format(pdict))
if 'sid' in pdict:
    y, name, usertype = isSession(pdict['sid'])
    if usertype != 'M':
        redirectTo('../index.html') # non manager
if method == 'POST':
    form = cgi.FieldStorage()
    uuid = form.getfirst('uuid')
    if uuid is not None: #удаление
        removeUser(uuid)
        redirectTo('./admins.py') #list of users
    else:
        name = form.getfirst("name", '')
        password = form.getfirst("password", '')
        hotel = form.getfirst("hotel", '')
        addUser(name, password, hotel, 'A1') # added admin
        redirectTo('./admins.py')
elif (method == "GET"): #list
    listfilename = os.path.join(path, 'list.templ')
    with open(listfilename, 'r') as f:
        html = f.read()
        template = Template(html)
        listr = listUsers('A1')
        #print(listr) #[(3, 'ace', 'A1')]
        print(template.render(list=listr, action="./admins.py", title=u'list of administrator'))