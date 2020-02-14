import os
import uuid

logders = 'lodgers.dat'
path = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(path, logders)

def newLodger(dataTuple):
    # print(dataTuple)
    uuidLodger = uuid.uuid1();
    row = str(uuidLodger)+ ',' + ','.join(dataTuple) + '\n'
    print(row)
    with open(filename, 'a') as fp:
        fp.write(row)
    return uuidLodger

def isLodger(uuidLodger: str):
    with open(filename, 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            ls = line.split(',')
            if ls[0] == uuidLodger:
                return True
    return False

def removeLodger(uuidLodger):
    with open(filename, 'r') as fp:
        lines = fp.readlines()
        with open(filename, 'w') as fp:
            for l in lines:
                ll = l.split(',')
                if ll[0] != uuidLodger:
                    fp.write(ll)

