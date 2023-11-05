# Создайте класс-функцию, который считает факториал числа при вызове экземпляра. Экземпляр должен запоминать последние k значений. 
# Параметр k передаётся при создании экземпляра. Добавьте метод для просмотра ранее вызываемых чисел и их факториалов.
# Доработаем задачу 1. Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.
import json


class Factorial:
    def __init__(self, k):
        self.k = k
        self.dict_result = {}

    def __call__(self, num):
        count = 1
        for i in range(1, num + 1):
            count *= i
        self.rem(num, count)
        return count

    def rem(self, num, result):
        if len(self.dict_result.values()) > self.k - 1:
            self.dict_result = dict(list(self.dict_result.items())[1:])
            self.dict_result.update({num: result})

    def memory(self):
        return self.dict_result

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('factorial.json', 'w') as f:
            json.dump(self.dict_result, f, indent=3)


f = Factorial(2)
with f as g:
    print(g(3))
    print(g(7))
    print(g(5))

print(f(3))
print(f(6))
print(f.memory())
print(f(5))
print(f.memory())