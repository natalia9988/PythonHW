# На семинаре про декораторы был создан логирующих декоратор. Он сохранял аргументы функции и результат её работы в файл. 
# Напишите аналогичный декоратор, но внутри используйте модуль logging.
import logging
logging.basicConfig(filename='logs.log',filemode='w',encoding='utf-8',level=logging.ERROR)
logger=logging.getLogger(__name__)



def log_dec(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logger.error(f'Ошибка {e} в функции {func.__name__} при аргументах {args}, {kwargs}')
        return None

    return wrapper


@log_dec
def my_func(storage, key, value=None):
    return storage[key]


@log_dec
def func_2(a, b):
    return a / b


d = func_2(5, 0)
f = {'f': '1', 'd': '3', 's': '5'}

print(my_func(f, 'a', 2))