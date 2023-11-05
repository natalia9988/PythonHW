# Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с псевдо именами и произведением чисел.
# Напишите функцию, которая создаёт из созданного ранее файла новый с данными в формате JSON. Имена пишите с большой буквы. 
# Каждую пару сохраняйте с новой строки.
import json


def to_json(old_file, new_file):
    with open(old_file, "r") as f:
        data = {i.split()[0].capitalize(): float(i.split()[1])
            for i in f.read().split("\n")}
    with open(new_file, "w") as new_file:
        json.dump(data, new_file, indent=4)


to_json("output.txt", "to_json_file.json")