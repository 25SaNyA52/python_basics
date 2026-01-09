# 1. Создание пустого словаря contacts
contacts = {}

# 2. Добавление информации о двух контактах
contacts['Anna Ivanovna'] = {
    'name': 'Anna Ivanovna',
    'phone': '+79001234567',
    'email': 'anna.ivanova@example.com'
}

contacts['Petr Sidorov'] = {
    'name': 'Petr Sidorov',
    'phone': '+79119876543',
    'email': 'petr.sidorov@example.com'
}

# 3. Распечатать информацию о контакте Анна Иванова
print("Информация о контакте 'Anna Ivanovna':")
print(contacts['Anna Ivanovna'])

# 4. Изменить номер телефона для Петра Сидорова
contacts['Petr Sidorov']['phone'] = '+79225551122'

# 5. Добавить ключ address для Анны Ивановой
contacts['Anna Ivanovna']['address'] = 'г. Москва, ул. Пушкина, д. 10'

# 6. Удалить ключ email для Петра Сидорова
del contacts['Petr Sidorov']['email']

# 7. Распечатать весь словарь contacts
print("\nВсе контакты после изменений:")
for name, contact_info in contacts.items():
    print(f"{name}: {contact_info}")
