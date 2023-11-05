# Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
# Дорабатываем задачу 1. Превратите внешнюю функцию в декоратор. 
# Он должен проверять входят ли переданные в функцию-угадайку числа в диапазоны [1, 100] и [1, 10]. 
# Если не входят, вызывать функцию со случайными числами из диапазонов.
from random import randint
from functools import wraps
#1
def ran_num(rnd_num, count_num):
    def guess():
        for i in range(count_num):
            input_num = int(input('введите число: '))
        if input_num > rnd_num:
            print('Меньше')
        elif input_num < rnd_num:
            print('Больше')
        else:
            print(rnd_num)
        return True
    return False

    return guess


# rnd = ran_num(4, 5)
# print(ran_num(4, 5)())

#2
def game_decor(func: callable):
    def wrapper(rnd_num, count_num):
        if not 1 <= rnd_num <= 100:
             rnd_num = randint(a=1, b=100)
        if not 1 <= count_num <= 10:
             count_num = randint(a=1, b=10)
        result = func(rnd_num, count_num)
        return result

    return wrapper


@game_decor
def guess(rnd_num, count_num):
    for i in range(count_num):
        input_num = int(input('введите число: '))
    if input_num > rnd_num:
        print('Меньше')
    elif input_num < rnd_num:
        print('Больше')
    else:
        print(rnd_num)
        return True
    return False


guess(101, 11)