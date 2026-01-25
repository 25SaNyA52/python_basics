# Базовый класс для всех геометрических фигур
class Shape:
    # Базовый класс для геометрических фигур.
    # Атрибуты:
    #     _color (str): цвет фигуры (защищенный атрибут)
    def __init__(self, color):
        # Инициализирует фигуру с заданным цветом.
        # Args:
        #     color (str): цвет фигуры
        self._color = color

    def get_area(self):
        # Вычисляет площадь фигуры.
        # Returns:
        #     float: площадь фигуры (0.0 для базового класса)
        return 0.0

    def get_perimeter(self):
        # Вычисляет периметр фигуры.
        # Returns:
        #     float: периметр фигуры (0.0 для базового класса)
        return 0.0

    def __str__(self):
        # Возвращает строковое представление фигуры.
        # Returns:
        #     str: информация о фигуре
        return f"Shape (Color: {self._color})"