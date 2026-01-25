# Класс Triangle - представляет треугольник
import math
from .shape import Shape  # Относительный импорт (с точкой!)

class Triangle(Shape):
    # Класс треугольника, наследуется от Shape.
    # Атрибуты:
    #     _color (str): цвет треугольника
    #     _a (float): первая сторона треугольника
    #     _b (float): вторая сторона треугольника
    #     _c (float): третья сторона треугольника

    def __init__(self, color, a, b, c):
        # Инициализирует треугольник с заданными сторонами.
        # Args:
        #     color (str): цвет треугольника
        #     a (float): первая сторона
        #     b (float): вторая сторона
        #     c (float): третья сторона
        # Raises:
        #     ValueError: если стороны не положительные или треугольник не существует
        super().__init__(color)

        # Валидация 1: все стороны должны быть положительными
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive")

        # Валидация 2: проверка неравенства треугольника
        # Сумма любых двух сторон должна быть СТРОГО больше третьей
        if (a + b <= c) or (a + c <= b) or (b + c <= a):
            raise ValueError("Invalid triangle! Sum of two sides must be > third.")

        self._a = a
        self._b = b
        self._c = c

    def get_perimeter(self):
        # Вычисляет периметр треугольника.
        # Formula: P = a + b + c
        # Returns:
        #     float: периметр треугольника
        return self._a + self._b + self._c

    def get_area(self):
        # Вычисляет площадь треугольника по формуле Герона.
        # Formula:
        #     1. s = (a + b + c) / 2 (полупериметр)
        #     2. S = √(s × (s - a) × (s - b) × (s - c))
        # Returns:
        #     float: площадь треугольника

        # Вычисляем полупериметр
        s = self.get_perimeter() / 2

        # Формула Герона
        area = math.sqrt(s * (s - self._a) * (s - self._b) * (s - self._c))
        return area

    def __str__(self):
        # Возвращает строковое представление треугольника.
        # Returns:
        #     str: информация о треугольнике
        return f"Triangle ({self._color}) | Sides: {self._a}, {self._b}, {self._c}"