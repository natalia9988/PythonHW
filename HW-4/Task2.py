#Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь, 
#где ключ — значение переданного аргумента, а значение — имя аргумента. 
#Если ключ не хешируем, используйте его строковое представление. 
names = ['str', 'int', 'bool', 'None', 'float', 'list', 'tuple', 'set']
vals = ['abc', 24, True, None, 3.14, [1, 2, 3], (1, 2, 3), {1, 2, 3}]


def form_dict(name_list, val_list):
    res_dict = {}
    for name, val in zip(name_list, val_list):
        try:
            res_dict[val] = name
        except TypeError:
            res_dict[str(val)] = name
    return res_dict


print(form_dict(names, vals))