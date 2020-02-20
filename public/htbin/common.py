import os
from jinja2 import Template
from session import existRecord, path
from db import getUser

def checkLogin(u, p):
    res = getUser(u, p)
    print (res)
    return res
    # def check(rec):
    #     r = rec.split(',')
    #     return (r[0].strip() == u) and (p == r[1].strip())
    # res, rec = existRecord(os.path.join(path, users), check)
    # reca = rec.split(',')
    # return res, reca[2].strip() #res, type (A || M)

def redirectTo(url, message = '', timeout = 0):
    filename = os.path.join(path, 'redirect.templ')
    with open(filename, 'r') as f:
        html = f.read()
        template = Template(html)
        print(template.render(url=url, message=message, timeout=timeout))
