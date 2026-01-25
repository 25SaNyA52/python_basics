
#Класс Circle - представляет круг
import math
from .shape import Shape  # Относительный импорт (с точкой!)


class Circle(Shape):
    # Класс круга, наследуется от Shape.
    # Атрибуты:
    #     _color (str): цвет круга
    #     _radius (float): радиус круга

    def __init__(self, color, radius):
        # Инициализирует круг с заданным цветом и радиусом.
        # Args:
        #     color (str): цвет круга
        #     radius (float): радиус круга
        # Raises:
        #     ValueError: если радиус не положительный
        super().__init__(color)  # Вызываем конструктор родительского класса
        # Валидация: радиус должен быть положительным
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self._radius = radius

    def get_area(self):
        # Вычисляет площадь круга.
        # Formula: S = π × r²
        # Returns:
        #     float: площадь круга
        return math.pi * (self._radius ** 2)

    def get_perimeter(self):
        # Вычисляет длину окружности (периметр круга).
        # Formula: P = 2 × π × r
        # Returns:
        #     float: длина окружности
        return 2 * math.pi * self._radius

    def __str__(self):
        # Возвращает строковое представление круга.
        # Returns:
        #     str: информация о круге
        return f"Circle ({self._color}) | R: {self._radius}"