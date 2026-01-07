# Пример модуля: my_module.py (представьте, что это отдельный файл)
# def greet(name):
#     return f"Привет, {name}!"

# Импорт модуля со стандартным именем
import math
print(math.sqrt(16))

# Импорт модуля с псевдонимом (alias)
import math as mt
print(mt.sqrt(25))

# Если у нас есть файл my_module.py с функцией greet:
# import my_module as mm
# print(mm.greet("Мир"))

# Импорт только функции sqrt из модуля math
from math import sqrt
print(sqrt(36))

# Импорт нескольких объектов
from math import sqrt, pi
print(f"Корень из 49: {sqrt(49)}")
print(f"Значение Pi: {pi}")

# Импорт объекта с псевдонимом
from math import cos as cosine
print(cosine(0))

# Пример установки популярного пакета 'requests' для выполнения HTTP-запросов
#!pip install requests

# После установки вы можете импортировать и использовать пакет
# import requests
# response = requests.get('https://www.google.com')
# print(f"Статус код Google: {response.status_code}")