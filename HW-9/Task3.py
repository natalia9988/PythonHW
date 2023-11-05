# Создайте декоратор с параметром. Параметр - целое число, количество запусков декорируемой функции.
def func_count(count):
    def func_dec(func):
        new_list = []

        def wrapper(*args, **kwargs):
            for i in range(count):
                result = func(*args, **kwargs)
                new_list.append(result)
            return new_list
        return wrapper
    return func_dec


@func_count(10)
def sum_func(a, b, *args, **kwargs):
    return a+b


print(sum_func(5, 3))