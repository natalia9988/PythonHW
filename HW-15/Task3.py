# Доработаем задачу 2. 
# Сохраняйте в лог файл раздельно: уровень логирования, дату события, имя функции (не декоратора), аргументы вызова, результат.
import logging

FORMAT= '{levelname},{asctime},{msg}'

logging.basicConfig(format=FORMAT, style='{',filename='logs.log',filemode='w',encoding='utf-8',level=logging.ERROR)
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