# Создаем список строк
inventory = ['apple', 'banana', 'orange', 'grape', 'pineapple', 'kiwi']

# Создаем пустой список для обработанных элементов
processed_items = []

# Используем цикл for с функцией enumerate (начинаем с 1)
for index, item in enumerate(inventory, start=1):
    # Проверяем условия
    if index % 2 == 0 and len(item) > 5:  # Четный индекс и длина > 5
        processed_items.append(f'{index}. Удлиненный {item}')
    elif index % 2 != 0 and item[0].lower() in ['a', 'e', 'i', 'o', 'u']:  # Нечетный и начинается с гласной
        processed_items.append(f'{index}. Стартует с гласной: {item}')
    else:  # Все остальные случаи
        processed_items.append(f'{index}. {item}')

# Распечатываем исходный список и результирующий список
print("Исходный список:", inventory)
print("Обработанные элементы:")
for item in processed_items:
    print(f"    '{item}'")