# -*- coding: utf-8 -*-
import os
import uuid
import cgi
from files import removeRecord, existRecord, addRecord, listRecords
from common import redirectTo
from jinja2 import Template

logders = 'lodgers.dat'
path = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(path, logders)

def newLodger(dataTuple):
    return addRecord(filename, dataTuple) # returns uuid

def isLodger(uuidLodger: str):
    return existRecord(filename, lambda line: line.split(',')[0] == uuidLodger)


def removeLodger(uuidLodger):
    removeRecord(filename, lambda line: line.split(',')[0] == uuidLodger)

method = os.environ['REQUEST_METHOD'].upper() #POST
print ("Content-type: text/html")
print ("")
if method == 'POST':
    form = cgi.FieldStorage()
    uuid = form.getfirst('uuid')
    if uuid is not None: # delete
        removeRecord(filename, lambda line: line.split(',')[0] == uuid)
        redirectTo('./lodger.py') #list of lodgers
    else:
        name=form.getfirst('name')
        lastname=form.getfirst('lastname')
        patronymic=form.getfirst('patronymic')
        tel=form.getfirst('tel')
        passport=form.getfirst('passport')
        birthday=form.getfirst('birthday')
        sex=form.getfirst('sex')
        res = addRecord(filename, (name, lastname, patronymic, tel, passport, birthday, sex))
        redirectTo('../index.html')
elif method == "GET": # list of lodgers 
    listfilename = os.path.join(path, 'list.templ')
    with open(listfilename, 'r') as f:
        html = f.read()
        template = Template(html)
        listr = listRecords(filename)
        print(template.render(list=listr, action='./lodger.py' title=u'list of lodgers Ю'))