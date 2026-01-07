temperature = 25

if temperature > 30:
    print("Очень жарко!")
elif temperature > 20:
    print("Тепло и приятно.")
elif temperature > 10:
    print("Прохладно.")
else:
    print("Холодно!")

# Пример с другой температурой
temperature = 5

if temperature > 30:
    print("Очень жарко!")
elif temperature > 20:
    print("Тепло и приятно.")
elif temperature > 10:
    print("Прохладно.")
else:
    print("Холодно!")

age = 18
status = "Совершеннолетний" if age >= 18 else "Несовершеннолетний"
print(f"Пользователь: {status}")

age = 16
status = "Совершеннолетний" if age >= 18 else "Несовершеннолетний"
print(f"Пользователь: {status}")

trafic_light_status = "зеленый"

match trafic_light_status:
    case "зеленый":
        print("Можно ехать.")
    case "желтый":
        print("Приготовьтесь.")
    case "красный":
        print("Стойте.")
    case _:
        print("Неизвестное состояние.")


team = ("добавить", "item_name", 10)

match team:
    case ("добавить", name, quantity):
        print(f"Добавляем {quantity} шт. {name}.")
    case ("удалить", name):
        print(f"Удаляем {name}.")
    case ("обновить", name, new_quantity):
        print(f"Обновляем {name} до {new_quantity} шт.")
    case _:
        print("Неизвестная команда.")

team = ("удалить", "старый_элемент")


match team:
    case ("добавить", name, quantity):
        print(f"Добавляем {quantity} шт. {name}.")
    case ("удалить", name):
        print(f"Удаляем {name}.")
    case ("обновить", name, new_quantity):
        print(f"Обновляем {name} до {new_quantity} шт.")
    case _:
        print("Неизвестная команда.")