#код для вывода данных из таблицы эксель.


import pyexcel as pe
sheet = pe.get_book(file_name="C:\Telebot\key.xls")
print(sheet)