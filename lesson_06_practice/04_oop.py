class Rectangle:
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    # Свойство для ширины
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if value <= 0:
            print("Ошибка: Значение должно быть больше 0!")
        else:
            self.__width = value

    # Свойство для высоты
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if value <= 0:
            print("Ошибка: Значение должно быть больше 0!")
        else:
            self.__height = value

    # Магический метод для строкового представления
    def __str__(self):
        return f"Прямоугольник {self.__width}x{self.__height}"

    # Магический метод для сложения (сумма площадей)
    def __add__(self, other):
        if isinstance(other, Rectangle):
            area_self = self.__width * self.__height
            area_other = other.__width * other.__height
            return area_self + area_other
        else:
            raise TypeError("Можно складывать только объекты Rectangle")

    # Дополнительный метод для вычисления площади
    def area(self):
        return self.__width * self.__height


# Тестирование класса
print("Тест 1: Создание прямоугольников и вывод")
rect1 = Rectangle(5, 4)
rect2 = Rectangle(10, 2)

print(rect1)  # Использует __str__
print(f"Площадь rect1: {rect1.area()}")
print(rect2)
print(f"Площадь rect2: {rect2.area()}")

print("\nТест 2: Сложение прямоугольников (сумма площадей)")
sum_areas = rect1 + rect2  # Использует __add__
print(f"Сумма площадей: {sum_areas}")

print("\nТест 3: Изменение ширины на положительное значение")
rect1.width = 8
print(f"После изменения ширины: {rect1}")
print(f"Новая площадь: {rect1.area()}")

print("\nТест 4: Попытка установить недопустимое значение")
rect1.width = -5  # Должно вызвать ошибку
print(f"После попытки изменения на -5: {rect1}")

print("\nТест 5: Изменение высоты")
rect1.height = 6
print(f"После изменения высоты: {rect1}")
print(f"Новая площадь: {rect1.area()}")

print("\nТест 6: Попытка установить нулевую высоту")
rect1.height = 0  # Должно вызвать ошибку
print(f"После попытки изменения на 0: {rect1}")