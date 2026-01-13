#Лямбда-функции (Анонимные Функции)
# Лямбда-функция для возведения числа в квадрат
square = lambda x: x * x
print(f"Квадрат 5: {square(5)}")

# Лямбда-функция для суммирования двух чисел
add = lambda a, b: a + b
print(f"Сумма 10 и 15: {add(10, 15)}")

#Лямбда-функции с map()
list_of_numbers = [1, 2, 3, 4, 5]

# Использование map() с лямбдой для удвоения каждого числа
doubled_numbers = list(map(lambda x: x * 2, list_of_numbers))
print(f"Удвоенные числа: {doubled_numbers}")

# Использование map() с лямбдой для возведения каждого числа в квадрат
squared_numbers = list(map(lambda x: x**2, list_of_numbers))
print(f"Квадраты чисел: {squared_numbers}")

#Лямбда-функции с filter()
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Использование filter() с лямбдой для отбора только четных чисел
even_numbers = list(filter(lambda x: x % 2 == 0, list_of_numbers))
print(f"Четные числа: {even_numbers}")

# Использование filter() с лямбдой для отбора чисел больше 5
numbers_greater_than_5 = list(filter(lambda x: x > 5, list_of_numbers))
print(f"Числа больше 5: {numbers_greater_than_5}")