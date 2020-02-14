import os
import uuid
from files import removeRecord, existRecord, addRecord

logders = 'lodgers.dat'
path = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(path, logders)

def newLodger(dataTuple):
    return addRecord(filename, dataTuple) # returns uuid

def isLodger(uuidLodger: str):
    return existRecord(filename, lambda line: line.split(',')[0] == uuidLodger)


def removeLodger(uuidLodger):
    removeRecord(filename, lambda line: line.split(',')[0] == uuidLodger)