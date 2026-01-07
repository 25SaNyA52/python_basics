# Пустой кортеж
empty_tuple = ()
print(f"Пустой кортеж: {empty_tuple}")
print(f"Тип пустого кортежа: {type(empty_tuple)}")

# Кортеж с целыми числами
numbers_tuple = (1, 2, 3, 4, 5)
print(f"Кортеж чисел: {numbers_tuple}")

# Кортеж с разными типами данных
mixed_tuple = (1, "привет", 3.14, True)
print(f"Смешанный кортеж: {mixed_tuple}")

single_element_not_tuple = (42) # Это int, а не кортеж
print(f"Тип (42): {type(single_element_not_tuple)}")

single_element_tuple = (42,)
print(f"Тип (42,): {type(single_element_tuple)}")
print(f"Кортеж из одного элемента: {single_element_tuple}")

my_colors = ("красный", "зеленый", "синий", "желтый")

# Доступ по индексу
print(f"Первый цвет: {my_colors[0]}") # красный
print(f"Последний цвет (отрицательный индекс): {my_colors[-1]}") # желтый

# Срезы
print(f"Первые два цвета: {my_colors[0:2]}") # ('красный', 'зеленый')
print(f"Все, кроме первого: {my_colors[1:]}") # ('зеленый', 'синий', 'желтый')

# Это вызовет ошибку TypeError!
# my_colors[0] = "фиолетовый"
# print(my_colors)

tuple_a = (1, 2)
tuple_b = (3, 4)

# Конкатенация (объединение)
combined_tuple = tuple_a + tuple_b
print(f"Объединенный кортеж: {combined_tuple}") # (1, 2, 3, 4)

# Повторение
repeated_tuple = tuple_a * 3
print(f"Повторенный кортеж: {repeated_tuple}") # (1, 2, 1, 2, 1, 2)

fruits = ("яблоко", "банан", "вишня")
print(f"Есть ли 'банан' в кортеже? {'банан' in fruits}") # True
print(f"Есть ли 'манго' в кортеже? {'манго' in fruits}") # False

coordinates = (10, 20)
x, y = coordinates
print(f"X: {x}, Y: {y}")

person_info = ("Анна", 30, "Москва")
name, age, city = person_info
print(f"Имя: {name}, Возраст: {age}, Город: {city}")

import sys

# Создадим список и кортеж с одинаковыми элементами
my_list = [1, 2, 3, 4, 5, "hello", True, 3.14]
my_tuple = (1, 2, 3, 4, 5, "hello", True, 3.14)

# Получим размер в байтах
size_of_list = sys.getsizeof(my_list)
size_of_tuple = sys.getsizeof(my_tuple)

print(f"Размер списка ({len(my_list)} элементов): {size_of_list} байт")
print(f"Размер кортежа ({len(my_tuple)} элементов): {size_of_tuple} байт")

# Создадим список и кортеж с большим количеством элементов для более явного сравнения
large_list = list(range(1000))
large_tuple = tuple(range(1000))

size_of_large_list = sys.getsizeof(large_list)
size_of_large_tuple = sys.getsizeof(large_tuple)

print(f"\nРазмер большого списка ({len(large_list)} элементов): {size_of_large_list} байт")
print(f"Размер большого кортежа ({len(large_tuple)} элементов): {size_of_large_tuple} байт")
