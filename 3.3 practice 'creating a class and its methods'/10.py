import math


class Point:
    """Класс для представления точки на координатной плоскости."""

    points = []

    def __init__(self, x: float, y: float) -> None:
        """
        Инициализируем координаты точки.

        :param x: Координата x точки.
        :param y: Координата y точки.
        """
        self.x = x
        self.y = y
        Point.points.append(self)

    def distance_from_origin(self) -> float:
        """Возвращает расстояние от начала координат до точки."""
        return math.sqrt(self.x ** 2 + self.y ** 2)

    def display(self) -> None:
        """Отображает координаты точки."""
        print(f"Point({self.x}, {self.y})")

    @classmethod
    def get_point_with_max_distance(cls):
        """Находит точку с максимальным расстоянием от начала координат
        и отображает ее."""
        if not cls.points:
            print("Нет созданных точек.")
            return

        max_distance_point = max(cls.points, key=lambda point: (
            point.distance_from_origin(), point.y))
        max_distance_point.display()


p1 = Point(4, 5)
p2 = Point(2, 4)
p3 = Point(5, 1)
p2.get_point_with_max_distance()
