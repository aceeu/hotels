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
        return False, '', ''
    recA = rec.split(',')
    return True, recA[1], recA[2] # name, type (A,M)

def newSession(user, type):
    return addRecord(filename, (user, type))

def endSession(sid):
    removeRecord(filename, lambda line: line.split(',')[0] == sid)
