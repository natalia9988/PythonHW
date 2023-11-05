class Archive:
    """
    Создайте класс Архив, который хранит пару свойств. Например, число и строку.
    При нового экземпляра класса, старые данные из ранее созданных экземпляров сохраняются в пару списков-архивов,
    которые также являются свойствами экземпляра.
    """
    instance = None

    def __new__(cls, *args, **kwargs):
    # применение свойств для класса
        if cls.instance is None:
            cls.instance = super().__new__(cls)
            cls.instance.archive_text = []
            cls.instance.archive_number = []
        else:
            cls.instance.archive_text.append(cls.instance.text)
            cls.instance.archive_number.append(cls.instance.number)
        return cls.instance

    def __init__(self, text, number):
        self.text = text
        self.number = number

    def __str__(self) -> str:
        return f"Text is {self.text} and number is {self.number}. Also {self.archive_text}, and {self.archive_number}"

    def __repr__(self) -> str:
        return f"Arhive({self.text}, {self.number})"
    
archive1 = Archive("Запись 1", 42)
archive2 = Archive("Запись 2", 3.14)