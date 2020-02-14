import cgi
import os
import json
from os import environ
from session import isSession

print ("Content-type: application/json")
print("")
# print ("<title>Hello</title>")
# print(environ['HTTP_COOKIE'])
key, pdict = cgi.parse_header('ddd=sss; ' + environ['HTTP_COOKIE'])
# print("<p>{}<p>".format(pdict))
if 'sid' in pdict:
    y, name = isSession(pdict['sid'])
    if y == True:
        res = dict(name=name)
        print(json.dumps(res))
    else:
        print("""{ }""")
else:
    print("""{ }""")
