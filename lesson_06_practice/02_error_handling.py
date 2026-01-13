def get_as_float(data_dict, key):

    # Безопасное извлечение значения из словаря по ключу и преобразование в float.
    #
    # Args:
    #     data_dict (dict): Словарь с данными
    #     key (str): Ключ для поиска значения
    #
    # Returns:
    #     str: Сообщение об успехе или ошибке

    try:
        # Пытаемся получить значение по ключу
        value = data_dict[key]

        # Пытаемся преобразовать значение в float
        float_value = float(value)

        # Если все успешно
        return f"Успех: Получено число {float_value}"

    except KeyError:
        # Обработка случая, когда ключа нет в словаре
        return f"Ошибка: Ключ '{key}' не найден!"

    except ValueError:
        # Обработка случая, когда значение нельзя превратить в число
        return f"Ошибка: Значение по ключу '{key}' нельзя превратить в число!"


# Создаем словарь с данными для тестирования
data = {"price": "10.5", "id": "abc"}

# Тестируем функцию
print("Тест 1 (ключ 'price'):")
print(get_as_float(data, "price"))
print()

print("Тест 2 (ключ 'id'):")
print(get_as_float(data, "id"))
print()

print("Тест 3 (ключ 'amount'):")
print(get_as_float(data, "amount"))