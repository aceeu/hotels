import os
from os import path
import uuid

def addRecord(filename, dataTuple): # data is tuple ('one', 'two', ....)
    uid = uuid.uuid1();
    row = str(uid)+ ',' + ','.join(dataTuple) + '\n'
    with open(filename, 'a') as fp:
        fp.write(row)
    return uid

def existRecord(filename, callback): # callback функция которая  принимает одну строку из файла и возвращает True или False
    if path.exists(filename) == False:
        return False, ''
    with open(filename, 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            l = line.strip()
            if callback(l):
                return True, l
        return False, ''

def removeRecord(filename, callback):
    with open(filename, 'r') as fp:
        lines = fp.readlines()
    with open(filename, 'w') as fp:
        for l in lines:
            if callback(l) == False:
                fp.write(l)