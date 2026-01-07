print("range(5) ->", list(range(5)))
print("range(2, 7) ->", list(range(2, 7)))
print("range(0, 10, 2) ->", list(range(0, 10, 2)))
print("range(5, 0, -1) ->", list(range(5, 0, -1)))

# Пример 1: range(stop) - от 0 до 4
print("Пример 1: range(5)")
for i in range(5):
    print(i)

# Пример 2: range(start, stop) - от 2 до 6
print("\nПример 2: range(2, 7)")
for i in range(2, 7):
    print(i)

# Пример 3: range(start, stop, step) - от 0 до 9 с шагом 2
print("\nПример 3: range(0, 10, 2)")
for i in range(0, 10, 2):
    print(i)

# Пример 4: Обратный отсчет с range(start, stop, step) - от 5 до 1 с шагом -1
print("\nПример 4: range(5, 0, -1) - Обратный отсчет")
for i in range(5, 0, -1):
    print(i)

# Создание списка из строки с помощью split()
text = "это пример строки для разделения"
words = text.split()
print(f"Исходная строка: '{text}'")
print(f"Список слов: {words}")

# Создание списка из строки с другим разделителем
numbers_str = "10;20;30;40;50"
numbers_list = numbers_str.split(';')
print(f"\nИсходная строка с разделителем ';': '{numbers_str}'")
print(f"Список чисел (как строки): {numbers_list}")

# Пример 1: Итерация по элементам списка
fruits = ["яблоко", "банан", "вишня"]
print("Элементы списка фруктов:")
for fruit in fruits:
    print(fruit)

# Пример 2: Итерация по списку чисел, полученному через split() и преобразованному в int
numbers_str = "100,200,300,400"
numbers_as_str_list = numbers_str.split(',')

print("\nСумма чисел в списке:")
total_sum = 0
for num_str in numbers_as_str_list:
    num = int(num_str) # Преобразуем строку в целое число
    total_sum += num
    print(f"Добавлено: {num}, Текущая сумма: {total_sum}")
print(f"Общая сумма: {total_sum}")

# Пример 1: Простой цикл while
print("Пример 1: Простой while цикл")
count = 0
while count < 5:
    print(count)
    count += 1 # Не забудьте изменить условие, чтобы избежать бесконечного цикла!

# Пример 2: Цикл while с условием для выхода
print("\nПример 2: while с условием выхода")
secret_number = 7
guess = 0
while guess != secret_number:
    # В реальном приложении здесь можно запросить ввод у пользователя
    # Для примера просто увеличиваем guess
    guess += 1
    if guess > 10: # Добавим ограничение, чтобы не было слишком долго
        print("Слишком много попыток!")
        break
    print(f"Попытка: {guess}")

if guess == secret_number:
    print(f"Угадано! Секретное число было {secret_number}")
else:
    print("Не удалось угадать секретное число.")

# Пример с 'break'
print("\nПример с 'break':")
for i in range(10):
    if i == 5:
        print("Встретили 5, выходим из цикла!")
        break # Выходит из цикла, когда i равно 5
    print(f"Текущее число (break): {i}")

# Пример с 'continue'
print("\nПример с 'continue':")
for i in range(10):
    if i % 2 == 0: # Если число четное
        print(f"Пропускаем четное число: {i}")
        continue # Пропускает оставшуюся часть текущей итерации
    print(f"Текущее число (continue - нечетное): {i}")

# Пример с 'break' в цикле while
print("\nПример с 'break' в цикле while:")
count_b = 0
while True:
    print(f"Счетчик (while break): {count_b}")
    count_b += 1
    if count_b > 3:
        print("Счетчик больше 3, выходим из цикла while!")
        break

# Пример с 'continue' в цикле while
print("\nПример с 'continue' в цикле while:")
count_c = 0
while count_c < 7:
    count_c += 1
    if count_c % 3 == 0:
        print(f"Пропускаем число кратное 3: {count_c}")
        continue
    print(f"Счетчик (while continue - не кратное 3): {count_c}")

# Пример 1: Блок `else` выполняется (нет оператора `break`)
print("--- Пример 1: Цикл завершается естественно ---")
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    print(f"Обрабатываем число: {num}")
else:
    print("Все числа обработаны. Блок 'else' выполнен.")

print("\n--- Пример 2: Блок `else` НЕ выполняется (используется `break`) ---")

# Пример 2: Блок `else` НЕ выполняется (используется оператор `break`)
search_list = [10, 20, 30, 40, 50]
target = 30

for item in search_list:
    print(f"Проверяем элемент: {item}")
    if item == target:
        print(f"Найдена цель {target}. Выходим из цикла.")
        break  # Прерываем цикл
else:
    print("Цель не найдена. Блок 'else' выполнен.") # Этот блок не будет выполнен

print("\n--- Пример 3: Блок `else` выполняется (цель не найдена) ---")

# Пример 3: Блок `else` выполняется (цель не найдена, `break` не сработал)
search_list_2 = [10, 20, 40, 50]
target_2 = 30

for item in search_list_2:
    print(f"Проверяем элемент: {item}")
    if item == target_2:
        print(f"Найдена цель {target_2}. Выходим из цикла.")
        break
else:
    print("Цель не найдена. Блок 'else' выполнен.")
