import os
import uuid
from files import removeRecord, existRecord, addRecord

path = os.path.dirname(os.path.abspath(__file__))
sessions = 'sessions.dat'
users = 'users.lst'
filename = os.path.join(path, sessions)

def isSession(sid):
    def check(rec):
        rs = rec.split(',')
        if rs[0] == sid:
            return True
        return False
    res, rec = existRecord(filename, check)
    if res == False:
        return False, ''
    return True, rec.split(',')[1]

def newSession(user):
    return addRecord(filename, (user, 'usertype'))

def endSession(sid):
    removeRecord(filename, lambda line: line.split(',')[0] == sid)

def checkLogin(u, p):
    def check(rec):
        r = rec.split(',')
        return (r[0].strip() == u) and (p == r[1].strip())
    res, rec = existRecord(os.path.join(path, users), check)
    return res
