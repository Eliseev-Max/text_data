#-*-coding:utf-8 -*-
"""Модуль содержит функцию, формирующую JSON-файл пользователей (из перечня users.json),
которым было выдано по одной книге из развёрноутого списка books.csv.
В созданном функцией JSON-файле представлена следующая информация о каждом пользователе:
* имя
* пол
* адрес
* книга"""

import csv
import json
import os

def distriBooks(books_in_csv, users_in_json):
    """Функция принимает аргументы:
        books_in_csv - имя CSV-файла, содержащего информацию о книгах,
        users_in_json - имя JSON-файла, содержащего информацию о пользователях.
        Функция создаёт на основе принятых файлов новый JSON-файл "result.json" 
        со структурой, приведённой в файле example.json
        Функция возвращает уведомление об успешном выполнении, если файл result.json был создан
        или выводит уведомление об ошибке, если файл не был создан"""

    # Проверка существования файлов с указанными в качестве аргументов функции именами
    assert os.path.exists(books_in_csv),"csv-файла, содержащего перечень книг, не существует"
    assert os.path.exists(users_in_json),"json-файла, содержащего данные о пользователях, не существует"
    books = []
    users = []
    # Парсинг CSV-файла
    with open(books_in_csv,"r+", encoding="utf-8") as r_file:
        file_reader = csv.DictReader(r_file, delimiter=",")
    # Формируем список книг с необходимыми нам параметрами
        for row in file_reader:
            book = dict(title=row['Title'],author=row['Author'],height=row['Height'])
            books.append(book)
    # Десериализация JSON-файла
    with open(users_in_json, 'r', encoding="utf-8") as jsonFile:
        users_full_info = json.load(jsonFile)
    # Формируем список пользователей с нужными нам параметрами
    for key in users_full_info:
        usr = dict(name = key["name"],gender = key["gender"],address = key["address"],books=[])
        users.append(usr)
    # Добавляем каждому пользователь по одной книге
    iter_books = iter(books)
    for add_book in users:
        add_book["books"].append(iter_books.__next__())
    # Сериализуем JSON-файл с пользователями, получившими книги
    if __name__ == "__main__":
        with open("result.json", 'w', encoding="utf-8") as write_to_file:
            json.dump(users,write_to_file, indent=4)
    if os.path.exists("result.json") == True:
        message = "Операция распределения книг выполнена успешно"
    else:
        message = "В ходе выполнения операции распределения книг возникла ошибка. Файл \"result.json\" не был создан"
    return print(message)
distriBooks("books.csv", "users.json")
