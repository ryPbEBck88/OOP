# Реализуйте класс Numbers, который предназначен для хранения
# произвольного количества чисел. Данный класс должен содержать:
#     1. метод __init__, принимающий произвольное количество чисел
#        и сохраняющий их внутри экземпляра;
#     2. метод add_number, которой принимает числовое значение
#        и добавляет его в конец коллекции экземпляра;
#     3. метод get_positive, который возвращает список всех
#        положительных чисел из коллекции экземпляра;
#     4. метод get_negative, который возвращает список всех
#        отрицательных чисел из коллекции экземпляра;
#     5. метод get_zeroes,  который возвращает список всех
#        нулевых значений из коллекции экземпляра.

class Numbers:
    """Класс для работы со списком чисел."""

    def __init__(self, *args: int) -> None:
        """Инициализируем список чисел.

        Параметры:
        *args (int): Переменное количество целых чисел,
        которые будут добавлены в список.
        """
        self.numbers = list(args)

    def add_number(self, number: int) -> None:
        """Добавляет число в конец списка.

        Параметры:
        number int: Число, которое будет добавлено в список.

        Исключение:
        ValueError: Если number не является целым числом.
        """
        if not isinstance(number, int):
            raise ValueError("number должен быть целым числом.")
        self.numbers.append(number)

    def get_positive(self) -> list[int]:
        """Возвращает список положительных чисел.

        Возвращает:
            list[int]: Список всех положительных чисел из списка self.numbers.
        """
        return [i for i in self.numbers if i > 0]

    def get_negative(self) -> list[int]:
        """Возвращает список отрицательных чисел.

        Возвращает:
            list[int]: Список всех отрицательных чисел из списка self.numbers.
        """
        return [i for i in self.numbers if i < 0]

    def get_zeroes(self) -> list[int]:
        """Возвращает список нулей.

        Возвращает:
            list[int]: Список всех нулей из списка self.numbers.
        """
        return [i for i in self.numbers if i == 0]


n1 = Numbers(1, 2, 3, 4, 5)
assert n1.numbers == [1, 2, 3, 4, 5]
n1.add_number(6)
assert n1.numbers == [1, 2, 3, 4, 5, 6]
assert n1.get_positive() == [1, 2, 3, 4, 5, 6]
assert n1.get_negative() == []
assert n1.get_zeroes() == []

n2 = Numbers(-1, 0, 12, -15, 11, 0)
assert n2.numbers == [-1, 0, 12, -15, 11, 0]
n2.add_number(0)
assert n2.get_positive() == [12, 11]
assert n2.get_zeroes() == [0, 0, 0]
assert n2.get_negative() == [-1, -15]

print("Good")
