import os
from jinja2 import Template
from session import existRecord, path, users

def checkLogin(u, p):
    def check(rec):
        r = rec.split(',')
        return (r[0].strip() == u) and (p == r[1].strip())
    res, rec = existRecord(os.path.join(path, users), check)
    reca = rec.split(',')
    return res, reca[2].strip() #res, type (A || M)

def redirectTo(url):
    filename = os.path.join(path, 'redirect.templ')
    with open(filename, 'r') as f:
        html = f.read()
        template = Template(html)
        print(template.render(url=url))
