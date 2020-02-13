import os
import uuid

path = os.path.dirname(os.path.abspath(__file__))
sessions = 'sessions.dat'
users = 'users.dat'


def isSession(sid):
    filename = os.path.join(path, sessions)
    with open(filename) as f_obj:
        lines = f_obj.readlines()
        for line in lines:
            sline = line.split(',')
            if (sline[0] == sid):
                return True, sline[1]
    return False, ''

def newSession(user):
    uuid_ = uuid.uuid3(uuid.NAMESPACE_DNS, user)
    filename = os.path.join(path, sessions)
    with open(filename, 'w+') as fp:
        fp.write('{},{}\n'.format(uuid_, user))
    return uuid_

def endSession(sid):
    print('sid: {}'.format(sid))
    filename = os.path.join(path, sessions)
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    with open(filename, 'w') as fp:
        for l in lines:
            ll = l.split(',')
            if ll[0] != sid:
                fp.write(ll)

def checkLogin(u, p):
    logged = False
    filename = os.path.join(path, users)
    with open(filename) as f_obj: lines = f_obj.readlines()
    for line in lines:
        items = line.split(',')
        logged = (u == items[0]) and (p == items[1])
        if logged: break
    return logged