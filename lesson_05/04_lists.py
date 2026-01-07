# Пустой список
my_empty_list = []
print(f"Пустой список: {my_empty_list}")

# Список чисел
numbers = [1, 2, 3, 4, 5]
print(f"Список чисел: {numbers}")

# Список строк
fruits = ["яблоко", "банан", "вишня"]
print(f"Список строк: {fruits}")

# Список разных типов данных
mixed_list = ["привет", 10, True, 3.14]
print(f"Смешанный список: {mixed_list}")

# Вложенный список
nested_list = [1, 2, ["a", "b"], 4]
print(f"Вложенный список: {nested_list}")

my_list = [10, 20, 30, 40, 50]

# Доступ к первому элементу
print(f"Первый элемент: {my_list[0]}")

# Доступ к третьему элементу
print(f"Третий элемент: {my_list[2]}")

# Доступ к последнему элементу (используя отрицательный индекс)
print(f"Последний элемент: {my_list[-1]}")

# Доступ ко второму с конца элементу
print(f"Второй с конца элемент: {my_list[-2]}")

my_list = ["a", "b", "c", "d", "e", "f"]

# Элементы со 2-го по 4-й (индексы 1, 2, 3)
print(f"Срез [1:4]: {my_list[1:4]}")

# Элементы с начала до 3-го (индексы 0, 1, 2)
print(f"Срез [:3]: {my_list[:3]}")

# Элементы с 3-го до конца
print(f"Срез [2:]: {my_list[2:]}")

# Копия списка
print(f"Копия списка: {my_list[:]}")

# Каждый второй элемент
print(f"Срез с шагом [::2]: {my_list[::2]}")

# Список в обратном порядке
print(f"Обратный список: {my_list[::-1]}")

my_list = [10, 20, 30, 40, 50]

# Изменение элемента по индексу
my_list[1] = 25
print(f"Список после изменения элемента: {my_list}")

# Изменение среза
my_list[2:4] = [35, 45]
print(f"Список после изменения среза: {my_list}")

my_list = [1, 2, 3]

# Добавление элемента в конец
my_list.append(4)
print(f"После append(4): {my_list}")

# Вставка элемента по индексу
my_list.insert(1, 1.5)
print(f"После insert(1, 1.5): {my_list}")

# Расширение списка другим списком
other_list = [5, 6]
my_list.extend(other_list)
print(f"После extend([5, 6]): {my_list}")

my_list = [10, 20, 30, 20, 40]

# Удаление элемента по значению
my_list.remove(20) # Удалит первое вхождение 20
print(f"После remove(20): {my_list}")

# Удаление элемента по индексу и получение его значения
popped_item = my_list.pop(1) # Удалит 30 (индекс 1)
print(f"После pop(1): {my_list}, удален: {popped_item}")

# Удаление последнего элемента
last_item = my_list.pop()
print(f"После pop(): {my_list}, удален: {last_item}")

# Удаление элемента с помощью del
del my_list[0] # Удалит 10
print(f"После del my_list[0]: {my_list}")

# Удаление среза с помощью del
another_list = [1, 2, 3, 4, 5]
del another_list[1:4]
print(f"После del another_list[1:4]: {another_list}")

# Очистка списка
my_list = [1,2,3]
my_list.clear()
print(f"После clear(): {my_list}")

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Длина списка
print(f"Длина list1: {len(list1)}")

# Объединение списков
combined_list = list1 + list2
print(f"Объединенный список: {combined_list}")

# Повторение списка
repeated_list = list1 * 2
print(f"Повторенный список: {repeated_list}")

# Проверка наличия элемента
print(f"Есть ли 3 в list1? {3 in list1}")
print(f"Есть ли 7 в list1? {7 in list1}")

# Итерация по списку
print("Элементы list1:")
for item in list1:
    print(item)

# Итерация с индексом
print("Элементы list2 с индексами:")
for index, item in enumerate(list2):
    print(f"Индекс {index}: {item}")

numbers = [3, 1, 4, 1, 5, 9, 2]

# Сортировка на месте
numbers.sort()
print(f"После numbers.sort(): {numbers}")

# Сортировка в обратном порядке
numbers = [3, 1, 4, 1, 5, 9, 2] # Сбрасываем для нового примера
numbers.sort(reverse=True)
print(f"После numbers.sort(reverse=True): {numbers}")

# Использование sorted() - возвращает новый список
unsorted_numbers = [3, 1, 4, 1, 5]
sorted_copy = sorted(unsorted_numbers)
print(f"Исходный список: {unsorted_numbers}")
print(f"Отсортированная копия: {sorted_copy}")

# Сортировка строк
words = ["банан", "яблоко", "вишня"]
words.sort()
print(f"Отсортированные слова: {words}")