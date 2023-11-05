# Доработайте класс прямоугольник из прошлых семинаров. 
# Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных). 
# Используйте декораторы свойств.
class Rect:
    def __init__(self, lenght, width=None):
        self._l = lenght
        if width:
            self._w = width
        else:
            self._w = lenght

    @property
    def l(self):
        return self._l

    @l.setter
    def l(self, value):
        if value > 0:
            self._l = value
        else:
            raise ValueError

    @property
    def w(self):
        return self._w

    @w.setter
    def w(self, value):
        if value > 0:
            self._w = value
        else:
            raise ValueError

    def per(self):
        return 2 * (self.l + self.w)

    def sq(self):
        return self.l * self.w


x1 = Rect(3, -2)
x2 = Rect(3, 2)
print(x1)
x2.w = -3
print(x2)