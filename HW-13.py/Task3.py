# Создайте класс с базовым исключением и дочерние классы-исключения: ошибка уровня, ошибка доступа.
class MyExcept(Exception):
    pass


class ErrorLevel(MyExcept):
    def __init__(self, admin_lvl, new_lvl) -> None:
        self.admin_lvl = admin_lvl
        self.new_lvl = new_lvl

    def __str__(self) -> str:
        return f"уровень админа {self.admin_lvl} должен быть меньше чем {self.new_lvl}"


class ErrorAccess(MyExcept):
    def __init__(self, id_user, name) -> None:
        self.id_user = id_user
        self.name = name

    def __str__(self) -> str:
        return f"нет пользователя с таким уровнем {self.id_user} и именем {self.name}"