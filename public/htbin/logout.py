import cgi
import os
import json
from os import environ
from session import endSession

print ("Content-type: application/json")
print("")
# print(environ['HTTP_COOKIE'])
key, pdict = cgi.parse_header('ddd=sss; ' + environ['HTTP_COOKIE'])
if 'sid' in pdict:
    endSession(pdict['sid'])
print("""{ }""")

