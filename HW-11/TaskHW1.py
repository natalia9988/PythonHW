import datetime

class MyStr(str):

    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.value = value
        instance.author = author
        instance.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        return instance
    def __str__(self)-> str:
        return f"{self.value} (Автор: {self.author}, Время создания: {self.time})"

    def __repr__(self) -> str:
        return f"MyStr({self.value},{self.author})"
    
event = MyStr("Завершилось тестирование", "John")
print(event)

# import time
# from datetime import datetime
# class MyStr(str):
#     """
#     Класс для создания строки с информацией об авторе и времени создания.

#     Атрибуты:
#     value (str): строковое значение.
#     author (str): имя автора.

#     Dunder методы:
#     __new__(cls, value, author): создает новый объект класса.
#     __str__(): возвращает строковое представление объекта класса.
#     __repr__(): возвращает строковое представление объекта класса для отладки.

#     """
# class MyStr(str):

#     def __new__(cls, value, author):
#         instance = super().__new__(cls, value)
#         instance.author = author
#         instance.time = time.time()
#         return instance

#     def __str__(self):
#         formatted_time = datetime.fromtimestamp(self.time).strftime('%Y-%m-%d %H:%M')
#         return f"{super().__str__()} (Автор: {self.author}, Время создания: {formatted_time})"

#     def __repr__(self):
#         return f"MyStr('{super().__str__()}', '{self.author}')"