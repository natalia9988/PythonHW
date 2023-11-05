# Напишите функцию, которая в бесконечном цикле запрашивает имя, личный идентификатор и уровень доступа (от 1 до 7). 
# После каждого ввода добавляйте новую информацию в JSON файл. Пользователи группируются по уровню доступа. 
# Идентификатор пользователя выступает ключём для имени. Убедитесь, что все идентификаторы уникальны независимо от уровня доступа. 
# При перезапуске функции уже записанные в файл данные должны сохраняться.
import json


def data(name: str, id: str, level: str, file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            users = json.load(f)
    except FileNotFoundError:
        users = {'1': {}, '2': {}, '3': {}, '4': {}, '5': {}, '6': {}, '7': {}}
    users[level][id] = name
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(users, f, ensure_ascii=False)


def request(file_name):
    while True:
        name = input('Введите имя: ')
        id = input('Введите id: ')
        level = input('Введите уровень: ')
        data(name, id, level, file_name)


request('users1.json')