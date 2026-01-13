# return

def greet(name):
    # Функция принимает имя и возвращает приветствие
    return f"Привет, {name}! Как дела?"

# Вызываем функцию greet с аргументом "Алексей" и выводим результат
print(greet("Алексей"))

# Функция с явным возвратом значения (числа)
def multiply(a, b):
    # Возвращает произведение двух чисел
    return a * b

# Вызываем функцию и сохраняем возвращенное значение в переменную `result`
result = multiply(5, 3)
print(f"Результат умножения: {result}")

# Функция без явного оператора return (возвращает None)
def print_greeting(name):
    # Просто печатает приветствие, ничего не возвращая явно
    print(f"Привет, {name}!")

# Вызываем функцию. `returned_value` получит значение None
returned_value = print_greeting("Ольга")
print(f"Функция без return вернула: {returned_value}") # Будет напечатано None

# Повторяющийся код
import math

# Вычисление площади для первого радиуса
radius1 = 5
area1 = math.pi * radius1**2
print(f"Площадь круга с радиусом {radius1}: {area1:.2f}") # Выводим площадь с двумя знаками после запятой

# Вычисление площади для второго радиуса
radius2 = 12.5
area2 = math.pi * radius2**2
print(f"Площадь круга с радиусом {radius2}: {area2:.2f}") # Повторяем тот же код

# Вычисление площади для третьего радиуса
radius3 = 7
area3 = math.pi * radius3**2
print(f"Площадь круга с радиусом {radius3}: {area3:.2f}") # И еще раз

# Решение с функциями (переиспользуемый код)
import math

def calculate_circle_area(radius):
    # Функция для вычисления площади круга по заданному радиусу
    return math.pi * radius**2

# Теперь мы просто вызываем функцию с разными радиусами
radius1 = 5
print(f"Площадь круга с радиусом {radius1}: {calculate_circle_area(radius1):.2f}")

radius2 = 12.5
print(f"Площадь круга с радиусом {radius2}: {calculate_circle_area(radius2):.2f}")

radius3 = 7
print(f"Площадь круга с радиусом {radius3}: {calculate_circle_area(radius3):.2f}")

# Параметры по умолчанию (Default Parameters)
def greet_with_city(name, city="Москва"):
    # Функция приветствует пользователя, используя город по умолчанию, если он не указан
    return f"Привет, {name} из {city}!"

# Вызов функции без указания города – используется значение по умолчанию "Москва"
print(greet_with_city("Анна"))
# Вызов функции с явным указанием города – значение по умолчанию переопределяется
print(greet_with_city("Борис", "Санкт-Петербург"))

# Аргументы переменной длины (*args)
def sum_numbers(*args):
    # Функция принимает любое количество чисел и возвращает их сумму
    total_sum = 0
    for num in args:
        total_sum += num
    return total_sum

# Вызов функции с разным количеством аргументов
print(sum_numbers(1, 2, 3))
print(sum_numbers(10, 20, 30, 40))
print(sum_numbers()) # Вызов без аргументов вернет 0

# Именованные аргументы переменной длины (**kwargs)

def user_info(**kwargs):
    # Функция принимает любое количество именованных аргументов и печатает их
    for key, value in kwargs.items():
        # Форматируем ключ для лучшей читаемости (например, 'user_name' -> 'User Name')
        print(f"{key.replace('_', ' ').capitalize()}: {value}")

# Вызов функции с различными именованными аргументами
user_info(name="Мария", age=30, city="Казань")
print("-" * 10)
user_info(product="Молоко", price=75, available=True) # Другой набор данных