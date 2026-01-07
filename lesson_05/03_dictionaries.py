# Пустой словарь
empty_dict = {}
print(f"Пустой словарь: {empty_dict}")

# Словарь с данными
person = {
    "name": "Алексей",
    "age": 30,
    "city": "Москва",
    "is_exist": True
}
print(f"Словарь с данными: {person}")

# Создание словаря с помощью функции dict()
animal = dict(type="собака", name="Бобик", age=5)
print(f"Словарь с dict(): {animal}")

print(f"Имя человека: {person['name']}")
print(f"Город человека: {person.get('city')}")

# Попытка доступа к несуществующему ключу
# print(person['country']) # Вызовет KeyError

# Метод .get() возвращает None или значение по умолчанию, если ключ не найден
print(f"Страна (с get(), по умолчанию None): {person.get('country')}")
print(f"Страна (с get(), по умолчанию 'Неизвестно'): {person.get('country', 'Неизвестно')}")

print(f"Имя человека: {person['name']}")
print(f"Город человека: {person.get('city')}")

# Изменение значения
person['age'] = 31
print(f"Измененный возраст: {person['age']}")

# Добавление нового элемента
person['occupation'] = 'Инженер'
print(f"Словарь после добавления: {person}")

# Удаление элемента по ключу с помощью del
del person['city']
print(f"Словарь после удаления города: {person}")

# Удаление элемента по ключу с помощью pop() (возвращает значение удаленного элемента)
occupation = person.pop('occupation')
print(f"Удаленная профессия: {occupation}")
print(f"Словарь после pop(): {person}")

# Удаление последнего добавленного элемента с помощью popitem() (возвращает пару ключ-значение)
# Примечание: до Python 3.7 popitem() удалял произвольный элемент
name_age_pair = person.popitem()
print(f"Удаленная пара (ключ, значение): {name_age_pair}")
print(f"Словарь после popitem(): {person}")

my_dict = {"a": 1, "b": 2, "c": 3}

print("Ключи:")
for key in my_dict:
    print(key)

print("\nЗначения:")
for value in my_dict.values():
    print(value)

print("\nПары ключ:значение:")
for key, value in my_dict.items():
    print(f"{key}: {value}")

print("\n items:")
for item in my_dict.items():
    print(f"{item}")

student = {
    "id": "S101",
    "name": "Анна",
    "major": "Компьютерные науки",
    "gpa": 3.8
}

print(f"Все ключи: {student.keys()}") #.keys(): возвращает объект, содержащий ключи словаря.
print(f"Все значения: {student.values()}") #.values(): возвращает объект, содержащий значения словаря.
print(f"Все пары: {student.items()}") #.items(): возвращает объект, содержащий пары ключ-значение.
print(f"Количество элементов: {len(student)}") #len(): возвращает количество элементов в словаре.

#key in dict: проверяет наличие ключа в словаре.
print(f"'name' есть в словаре? {'name' in student}")
print(f"'age' есть в словаре? {'age' in student}")