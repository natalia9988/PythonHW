# Создайте класс-генератор. Экземпляр класса должен генерировать факториал числа в диапазоне от start до stop с шагом step. 
# Если переданы два параметра, считаем step=1. Если передан один параметр, также считаем start=1.
class FactorialGen:
    def __init__(self, *args) -> None:
        if len(args) == 1:
            self.start = 1
            self.step = 1
            self.stop = args[0]
        elif len(args) == 2:
            self.start, self.stop = args
            self.step = 1
        else:
            self.start, self.stop, self.step = args

    def __iter__(self):
        return self

    def __next__(self):
        while self.start < self.stop+1:
            count = 1
            for j in range(1, self.start+1):
                count *= j
            self.start += self.step
            return count
        raise StopIteration


f = FactorialGen(5,9,2)
for i in f:
    print(i)