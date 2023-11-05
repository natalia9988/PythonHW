# Создайте класс прямоугольник. Класс должен принимать длину и ширину при создании экземпляра. 
# У класса должно быть два метода, возвращающие периметр и площадь. 
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.
class Rect:
    def __init__(self, lenght, width=None):
        self.l = lenght
        if width:
            self.w = width
        else:
            self.w = lenght

    def per(self):
        return 2 * (self.l + self.w)

    def sq(self):
        return self.l * self.w


x1 = Rect(3, 2)
x2 = Rect(3)
print(x1.per(), x1.sq())
print(x2.per(), x2.sq())