# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п. 
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса. 
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.
class Animals:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        return f"{self.name}"


class Kopyta(Animals):
    def __init__(self, name, weight_up):
        self.name = name
        self.weight_up = weight_up

    def print_info(self):
        return f"{self.name} {self.weight_up}"


class Cat(Animals):
    def __init__(self, color: str, age: int, name: str):
        self.color = color
        self.age = age
        self.name = name

    def print_info(self):
        return f'{self.color} {self.age} {self.name}'


class Dog(Animals):
    def __init__(self, poroda: str, xvost: str, name: str):
        self.poroda = poroda
        self.xvost = xvost
        self.name = name

    def print_info(self):
        return f'{self.poroda} {self.xvost} {self.name}'


class Horse(Animals):
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def print_info(self):
        return f'{self.color} {self.name}'