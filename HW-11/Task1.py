# Создайте класс МояСтрока где будут доступны все возможности str и дополнительно хранится имя автора строки и время создания (time.time)
import datetime

class MyStr(str):

    def __new__(cls, value, name):
        instance = super().__new__(cls, value)
        instance.name = name
        instance.time = datetime.datetime.now()
        return instance


a = MyStr('Hello', 'Andrey')
print(a.time)
b = MyStr('ghg','hghg')
print(b.time)   