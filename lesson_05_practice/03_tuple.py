# Создаем кортеж с данными
numbers_data = (15, 22, 10, 30, 5, 25, 18)

# 1. Вычисляем сумму всех элементов кортежа
sum_numbers = sum(numbers_data)

# 2. Находим среднее арифметическое элементов
average = sum_numbers / len(numbers_data)

# 3. Определяем максимальное и минимальное значения в кортеже
max_value = max(numbers_data)
min_value = min(numbers_data)

# 4. Выводим все полученные результаты на экран
print("Анализ числового кортежа:")
print(f"Кортеж: {numbers_data}")
print(f"Сумма всех элементов: {sum_numbers}")
print(f"Среднее арифметическое: {average}")
print(f"Максимальное значение: {max_value}")
print(f"Минимальное значение: {min_value}")