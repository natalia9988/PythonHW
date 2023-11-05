# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader. 
# Дополните id до 10 цифр незначащими нулями. В именах первую букву сделайте прописной. 
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь. 
# Имя исходного и конечного файлов передавайте как аргументы функции.
import json


def csv_to_json(csv_file, json_file):
    with open(csv_file, "r") as f:
        data = []
        for line in f:
            if line == "\n":
                continue
            name, id, lvl = line.split(",")
            data.append({"name": name.lower(), "id": f"{int(id):010}",
                            "lvl": lvl[:-1], "hash": hash(name+id)})
    with open(json_file, "w") as f:
        json.dump(data, f, indent=4)
csv_to_json("users.csv", "from_csv.json")