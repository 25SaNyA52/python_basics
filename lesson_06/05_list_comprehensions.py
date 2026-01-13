#Списковые Включения (List Comprehensions)

# Создание списка квадратов чисел от 0 до 9
squares = [x**2 for x in range(10)]
print(f"Квадраты: {squares}")

# Создание списка четных чисел от 0 до 9 с использованием условия `if`
even_numbers = [x for x in range(10) if x % 2 == 0]
print(f"Четные: {even_numbers}")

# Создание списка пар (число, квадрат) для чисел от 0 до 4
pair_squares = [(x, x**2) for x in range(5)]
print(f"Пары (число, квадрат): {pair_squares}")

#Списковое включение с if/else
list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Пример: удвоить четные числа и оставить нечетные как есть
# `x * 2 if x % 2 == 0 else x` - это выражение, которое применяется к каждому `x`
transformed_numbers = [x * 2 if x % 2 == 0 else x for x in list_of_numbers]
print(f"Преобразованные числа: {transformed_numbers}")