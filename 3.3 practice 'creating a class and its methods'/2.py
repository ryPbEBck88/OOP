# Создайте класс Rectangle, который имеет следующие методы:
#     1. метод __init__, который устанавливает значения атрибутов width и height
#     2. метод area, который возвращает площадь прямоугольника
#     3. метод perimeter , который возвращает периметр прямоугольника
from typing import Union

class Rectangle:
    def __init__(self, width: Union[int, float], height: Union[int, float]) -> None:
        """Инициализируем переменные"""
        self.width = width
        self.height = height

    def area(self) -> Union[int, float]:
        """Находим площадь прямоугольника"""
        return self.width * self.height

    def perimeter(self) -> Union[int, float]:
        """Находим периметр прямоугольника"""
        return (self.width + self.height) * 2


r1 = Rectangle(2, 3)
assert r1.width == 2
assert r1.height == 3
assert r1.perimeter() == 10
assert r1.area() == 6

r2 = Rectangle(10, 0.5)
assert r2.width == 10
assert r2.height == 0.5
assert r2.perimeter() == 21.0
assert r2.area() == 5.0
print("Good")
