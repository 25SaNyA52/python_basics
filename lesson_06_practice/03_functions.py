# Создаем список чисел от 1 до 20
numbers = list(range(1, 21))

# Отфильтруем только нечетные числа с помощью filter()
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

# Возведем каждое нечетное число в куб с помощью map()
cubed_odds = list(map(lambda x: x ** 3, odd_numbers))

# Выводим результаты
print("Исходный список чисел от 1 до 20:")
print(numbers)
print("\nНечетные числа из списка:")
print(odd_numbers)
print("\nКубы нечетных чисел:")
print(cubed_odds)