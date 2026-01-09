# 1. Запрашиваем у пользователя строку с названиями городов
cities_input = input("Введите 5 городов через запятую: ")

# 2. Преобразуем строку в список городов с помощью split()
cities_list = cities_input.split(',')

# Очищаем города от лишних пробелов
cities_list = [city.strip() for city in cities_list]

# 3. Используем цикл for с функцией range() для прохода по списку
for i in range(len(cities_list)):
    # Получаем город по индексу
    city = cities_list[i]

    # Проверяем, содержит ли город букву 'a' (без учета регистра)
    if 'a' in city.lower():
        print(f"Город {i + 1}: {city} (в этом городе есть 'a')")
    else:
        print(f"Город {i + 1}: {city}")