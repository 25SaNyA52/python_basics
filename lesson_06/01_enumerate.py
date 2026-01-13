# Что такое функция enumerate
fruits = ["яблоко", "банан", "вишня", "дыня"]

print("Пример использования enumerate:")
for index, fruit in enumerate(fruits):
    print(f"Индекс: {index}, Элемент: {fruit}")

print("\nПример использования enumerate со стартовым индексом (например, с 1):")
for index, fruit in enumerate(fruits, start=1):
    print(f"Индекс: {index}, Элемент: {fruit}")

# Использование enumerate с различными итерируемыми объектами

print("\nПример использования enumerate со строкой:")
my_string = 'Python'
for index, char in enumerate(my_string):
    print(f"Индекс: {index}, Символ: {char}")

print("\nПример использования enumerate с кортежем:")
my_tuple = ('яблоко', 'банан', 'вишня')
for index, item in enumerate(my_tuple):
    print(f"Индекс: {index}, Элемент: {item}")

print("\nПример использования enumerate со словарем (по парам ключ-значение):")
my_dict = {'a': 1, 'b': 2, 'c': 3}
for index, (key, value) in enumerate(my_dict.items()):
    print(f"Индекс: {index}, Ключ: {key}, Значение: {value}")

print("\nПример использования enumerate со словарем (по ключам):")
for index, key in enumerate(my_dict.keys()):
    print(f"Индекс: {index}, Ключ: {key}")

print("\nПример использования enumerate со словарем (по значениям):")
for index, value in enumerate(my_dict.values()):
    print(f"Индекс: {index}, Значение: {value}")

# Примеры использования в реальных задачах

print("\n--- Примеры использования enumerate в реальных задачах ---\n")

# Пример 1: Создание нового списка кортежей (индекс, элемент), начиная с индекса 1
print("Пример 1: Создание списка кортежей с индексами (начиная с 1)\n")
tasks = ['Купить продукты', 'Заплатить по счетам', 'Позвонить другу']
indexed_tasks = []
for index, task in enumerate(tasks, start=1):
    indexed_tasks.append((index, task))
print(f"Исходный список задач: {tasks}")
print(f"Список задач с индексами: {indexed_tasks}\n")

# Пример 2: Обновление элементов списка по индексу (умножение четных чисел на 2)
print("Пример 2: Обновление четных элементов списка по индексу\n")
numbers = [10, 25, 30, 45, 50]
print(f"Исходный список чисел: {numbers}")
for index, num in enumerate(numbers):
    if num % 2 == 0:
        numbers[index] = num * 2
print(f"Обновленный список чисел: {numbers}\n")

# Пример 3: Создание словаря, где ключи - индексы, значения - элементы списка
print("Пример 3: Создание словаря из списка с индексами в качестве ключей\n")
items = ['яблоко', 'банан', 'вишня']
item_dict = {}
for index, item in enumerate(items):
    item_dict[index] = item
print(f"Исходный список элементов: {items}")
print(f"Словарь элементов с индексами: {item_dict}")

# Сравнение с range(len())

my_list = ['a', 'b', 'c', 'd']

print("\n--- Использование range(len()) для итерации ---")
for i in range(len(my_list)):
    item = my_list[i]
    print(f"Индекс: {i}, Элемент: {item}")

my_list = ['a', 'b', 'c', 'd']

print("\n--- Использование enumerate() для итерации ---")
for index, item in enumerate(my_list):
    print(f"Индекс: {index}, Элемент: {item}")

