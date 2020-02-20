import sqlite3
import os

path = os.path.dirname(os.path.abspath(__file__))
hotelsfilename = os.path.join(path, 'hotels.db')

conn = sqlite3.connect(hotelsfilename)
cursor = conn.cursor()

#user
def addUser(name, password , type):
    try:
        cursor.execute("""INSERT INTO users (name, password, type) VALUES ('{}', '{}', '{}')""".format(name, password, 'A1'))
        conn.commit()
    except sqlite3.IntegrityError:
        pass

def listUsers(type):
    cursor.execute("SELECT id, name, type FROM users WHERE type=?", [(type)])
    return cursor.fetchall()

def removeUser(idu):
    try:
        cursor.execute("DELETE FROM users WHERE id=?", [(idu)])
        conn.commit()
    except sqlite3.IntegrityError:
        pass
# hotel
def addHotel(name, floors, count, country, city, street, house):
    try:
        cursor.execute("""INSERT INTO hotels(name, floors, count, country, city, street, house)
        VALUES('{}', {}, {}, '{}', '{}', '{}','{}')""".format(name, floors, count, country, city, street, house))
        conn.commit()
    except sqlite3.IntegrityError:
        pass

def listHotels():
    cursor.execute("SELECT id, name, country, city, street FROM hotels")
    return cursor.fetchall()

def removeHotel(idu):
    id = int(idu)
    try:
        cursor.execute("DELETE FROM hotels WHERE id=?", [(id)])
        conn.commit()
    except sqlite3.IntegrityError:
        pass

def addLodger(dataTuple):
    try:
        cursor.execute("""INSERT INTO lodgers(name, lastname, patronymic, tel, passport, birthday, sex)
        VALUES('{}', '{}', '{}','{}','{}','{}', {})""".format(*dataTuple))
    except sqlite3.IntegrityError:
        pass

def listLodgers():
    cursor.execute("SELECT name, lastname, payronymic, tel, passport FROM lodgers")
    return cursor.fetchall()

def removeLodger(uuidLodger):
    id = int(uuidLodger)
    try:
        cursor.execute("DELETE FROM lodgers WHERE id=?", [(id)])
        conn.commit()
    except sqlite3.IntegrityError:
        pass
