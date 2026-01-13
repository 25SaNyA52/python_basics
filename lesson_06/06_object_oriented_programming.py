class Car:
    pass

# Создание объектов (экземпляров класса)
my_car = Car()
your_car = Car()

print(type(my_car)) # <class '__main__.Car'>

class Car:
    # Атрибут класса (пишется прямо в теле класса)
    # Указываем тип через двоеточие
    wheels: int = 4

    def __init__(self, brand: str, model: str, year: int):
        # Атрибуты экземпляра (пишутся в конструкторе через self)
        # Хорошая практика — типизировать аргументы и сами атрибуты
        # self.brand: str — это указание, что атрибут будет строкой
        self.brand: str = brand
        self.model: str = model
        self.year: int = year

# Создаем объекты с разными данными
tesla: Car = Car("Tesla", "Model 3", 2023)
bmw: Car = Car("BMW", "M5", 2022)

print(f"Машина 1: {tesla.brand} {tesla.model}, Колес: {tesla.wheels}")
print(f"Машина 2: {bmw.brand} {bmw.model}, Колес: {bmw.wheels}")

#Что такое self
class Dog:
    def __init__(self, name: str):
        self.name: str = name

    def bark(self):
        # Используем self, чтобы обратиться к имени конкретной собаки
        print(f"{self.name} говорит: Гав!")

dog1 = Dog("Бобик")
dog1.bark() # self будет указывать на dog1

#инкапсуляция
class BankAccount:
    def __init__(self, balance: float) -> None:
        self.__balance: float = balance # Приватный атрибут

    def deposit(self, amount: float) -> None:
        # Проверка логики: сумма должна быть положительной
        if amount > 0:
            self.__balance += amount
            print(f"Пополнено на {amount}. Баланс: {self.__balance}")
        else:
            print(f"Ошибка: сумма {amount} недопустима для пополнения.")

    def get_balance(self) -> float:
        return self.__balance

account: BankAccount = BankAccount(1000.0)

# 1. Работающий пример
account.deposit(500.0)

# 2. Примеры, когда deposit НЕ сработает (из-за условия if amount > 0)
account.deposit(-100.0) # Отрицательное число
account.deposit(0.0)    # Ноль

# 3. Проверяем итоговый баланс (должен остаться 1500.0)
print(f"Итоговый баланс: {account.get_balance()}") # Правильный способ получения данных

# 4. Прямой доступ через __balance вызовет ошибку
# print(account.__balance) # AttributeError

# 5. Способ "обойти" защиту (Name Mangling)
# Python переименовывает атрибут в _ИмяКласса__имяАтрибута
print(f"Доступ через mangling: {account._BankAccount__balance}")

# ВАЖНО: Так делать крайне не рекомендуется.
# Это нарушает принципы ООП и может привести к поломке логики класса.

#Наследование (Inheritance)
#Пример 1: Базовое наследование и super()
class Employee:
    def __init__(self, name: str, salary: float) -> None:
        self.name: str = name
        self.salary: float = salary

    def get_info(self) -> str:
        return f"Сотрудник: {self.name}, Зарплата: {self.salary}"

class Developer(Employee):
    def __init__(self, name: str, salary: float, language: str) -> None:
        # Вызываем конструктор родителя для name и salary
        super().__init__(name, salary)
        self.language: str = language

    def get_info(self) -> str:
        # Дополняем метод родителя
        base_info = super().get_info()
        return f"{base_info}, Язык: {self.language}"

class Manager(Employee):
    def __init__(self, name: str, salary: float, team_size: int) -> None:
        super().__init__(name, salary)
        self.team_size: int = team_size

    def get_info(self) -> str:
        return f"Менеджер: {self.name}, Команда: {self.team_size} чел."

# 1. Пример использования БАЗОВОГО класса
eml: Employee = Employee("Алексей", 80000.0)
print(eml.get_info())

# 2. Пример использования ПОТОМКОВ
dev: Developer = Developer("Иван", 150000.0, "Python")
manager: Manager = Manager("Мария", 200000.0, 5)
print(dev.get_info())
print(manager.get_info())

#Пример 2: Множественное наследование и MRO
import json

class JsonMixin:
    """Примесь, добавляющая метод для превращения атрибутов в JSON."""
    def to_json(self) -> str:
        # self.__dict__ содержит все атрибуты экземпляра
        return json.dumps(self.__dict__, ensure_ascii=False)

# Ветка 1: Продукты
class BaseItem:
    def __init__(self, item_id: int) -> None:
        self.item_id = item_id

class Product(BaseItem, JsonMixin): # Наследование от основы и примеси
    def __init__(self, item_id: int, name: str, price: float) -> None:
        super().__init__(item_id)
        self.name = name
        self.price = price

# Ветка 2: Пользователи
class UserAccount:
    def __init__(self, username: str) -> None:
        self.username = username

class User(UserAccount, JsonMixin): # Наследование от основы и примеси
    def __init__(self, username: str, email: str) -> None:
        super().__init__(username)
        self.email = email

# Использование
p: Product = Product(101, "Кофе", 450.0)
u: User = User("ivan_admin", "admin@web.com")

print(p.to_json()) # Метод Mixin работает для Продукта
# print(u.to_json()) # Этот же метод работает для Пользователя

#Композиция сущностей
class Phone:
    def call(self, number: str) -> None:
        print(f"Звоню на номер {number}...")

class Camera:
    def take_photo(self) -> None:
        print("Чииииииз! Фото сохранено.")

# Смартфон — это и телефон, и камера одновременно
class Smartphone(Phone, Camera):
    def search_internet(self, query: str) -> None:
        print(f"Ищу в Google: {query}")

iphone: Smartphone = Smartphone()
iphone.call("8-800-555-35-35")
iphone.take_photo()

#Method Resolution Order
class A:
    def say(self): print("A")

class B(A):
    def say(self): print("B")

class C(A):
    def say(self): print("C")

class D(B, C): # Порядок родителей: B, затем C
    pass

# Использование __mro__ (атрибут)
print(D.__mro__)

# Использование .mro() (метод)
print(D.mro())

#Полиморфизм (Polymorphism)
import math

class Shape:
    """Базовый класс, задающий 'интерфейс'."""
    def area(self) -> float:
        # Мы выбрасываем ошибку, чтобы заставить программиста
        # переопределить этот метод в дочерних классах
        raise NotImplementedError("Метод area() должен быть переопределен")

class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side: float = side

    def area(self) -> float:
        return self.side ** 2 # Своя реализация для квадрата

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius: float = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2) # Своя реализация для круга

def print_area(shape: Shape) -> None:
    """
    Эта функция полиморфна: ей не важно, квадрат это или круг.
    Она просто просит объект 'вычислить площадь'.
    """
    print(f"Площадь фигуры: {shape.area():.2f}")

shapes: list[Shape] = [Square(5), Circle(3), Square(10)]

for s in shapes:
    print_area(s)

#Duck Typing ("Утиная типизация")
class CreditCard:
    def pay(self, amount: float) -> None:
        print(f"Оплата {amount} через Кредитную карту")

class PayPal:
    def pay(self, amount: float) -> None:
        print(f"Оплата {amount} через PayPal")

class Crypto:
    def pay(self, amount: float) -> None:
        print(f"Оплата {amount} через Криптовалюту")

# Эта функция НЕ ПРОВЕРЯЕТ тип объекта.
# Ей просто нужно, чтобы у объекта был метод .pay()
def process_payment(payment_method: any, amount: float) -> None:
    payment_method.pay(amount)

# Объекты разных классов, НЕ имеющие общего предка
methods = [CreditCard(), PayPal(), Crypto()]

for method in methods:
    process_payment(method, 100.0)

#Геттеры, Сеттеры и @property

class ClassicPerson:
    def __init__(self, age: int) -> None:
        self.__age: int = age

    # Геттер - метод для чтения
    def get_age(self) -> int:
        return self.__age

    # Сеттер - метод для записи с проверкой
    def set_age(self, value: int) -> None:
        if 0 < value < 120:
            self.__age = value
        else:
            print("Ошибка: Неверный возраст")

p = ClassicPerson(20)
p.set_age(25)            # Неудобный синтаксис (вызов функции)
print(p.get_age())


class ModernPerson:
    def __init__(self, age: int) -> None:
        self.__age: int = age

    @property
    def age(self) -> int:
        """Декоратор превращает метод в атрибут (геттер)."""
        print("Логика при чтении...")
        return self.__age

    @age.setter
    def age(self, value: int) -> None:
        """Сеттер позволяет менять значение через обычное присваивание."""
        if 0 < value < 120:
            print(f"Устанавливаем возраст: {value}")
            self.__age = value
        else:
            print("Ошибка: Неверный возраст")

p = ModernPerson(20)
p.age = 30               # Выглядит как работа с атрибутом, но внутри работает метод
print(p.age)

#Магические методы (Dunder Methods)

class Vector:
    def __init__(self, x: float, y: float) -> None:
        # Срабатывает при: v = Vector(1, 2)
        self.x = x
        self.y = y

    def __str__(self) -> str:
        # Срабатывает при: print(v)
        return f"Вектор({self.x}, {self.y})"

    def __add__(self, other: 'Vector') -> 'Vector':
        # Срабатывает при: v1 + v2
        return Vector(self.x + other.x, self.y + other.y)

    def __len__(self) -> int:
        # Срабатывает при: len(v)
        return 2

# Итог: Ты просто "наполняешь" смыслом готовые команды Python.
v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1)         # Python сам вызвал v1.__str__()
print(v1 + v2)    # Python сам вызвал v1.__add__(v2)
print(len(v1))    # Python сам вызвал v1.__len__()