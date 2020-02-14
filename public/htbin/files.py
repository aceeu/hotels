import os
import uuid

def addRecord(filename, dataTuple): # data is tuple ('one', 'two', ....)
    uid = uuid.uuid1();
    row = str(uid)+ ',' + ','.join(dataTuple) + '\n'
    with open(filename, 'a') as fp:
        fp.write(row)
    return uid

def existRecord(filename, callback): # callback функция которая  принимает одну строку из файла и возвращает True или False
    with open(filename, 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            if callback(line):
                return True, line
        return False, ''

def removeRecord(filename, callback):
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    with open(filename, 'w') as fp:
        for l in lines:
            if callback(l) == False:
                fp.write(l)