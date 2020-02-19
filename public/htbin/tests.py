from common import checkLogin
from db import listHotels, addHotel, removeHotel


res, type = checkLogin('Admin', 'Admin')
print(res)

addHotel(1, 2, "Россия", "Чебоксары", "Пролетарская", "1")
print(listHotels())

