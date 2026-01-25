# Класс Rectangle - представляет прямоугольник
from .shape import Shape  # Относительный импорт (с точкой!)

class Rectangle(Shape):
    # Класс прямоугольника, наследуется от Shape.
    # Атрибуты:
    #     _color (str): цвет прямоугольника
    #     _width (float): ширина прямоугольника
    #     _height (float): высота прямоугольника
    def __init__(self, color, width, height):
        # Инициализирует прямоугольник с заданными параметрами.
        # Args:
        #     color (str): цвет прямоугольника
        #     width (float): ширина прямоугольника
        #     height (float): высота прямоугольника
        # Raises:
        #     ValueError: если ширина или высота не положительные
        super().__init__(color)
        # Валидация: ширина и высота должны быть положительными
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self._width = width
        self._height = height

    def get_area(self):
        # Вычисляет площадь прямоугольника.
        # Formula: S = width × height
        # Returns:
        #     float: площадь прямоугольника
        return self._width * self._height

    def get_perimeter(self):
        # Вычисляет периметр прямоугольника.
        # Formula: P = 2 × (width + height)
        # Returns:
        #     float: периметр прямоугольника
        return 2 * (self._width + self._height)

    def __str__(self):
        # Возвращает строковое представление прямоугольника.
        # Returns:
        #     str: информация о прямоугольнике
        return f"Rectangle ({self._color}) | {self._width} x {self._height}"