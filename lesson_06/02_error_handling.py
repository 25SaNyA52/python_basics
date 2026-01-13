# # 1. Базовый блок try-except
# # Пример 1: Деление на ноль
#
# try:
#     result = 10 / 0
#     print(result)
# except ZeroDivisionError:
#     print("Ошибка: Нельзя делить на ноль!")
#
# print("Программа продолжает работу после обработки ошибки.")
#
# # Пример 2: Несколько исключений
#
# try:
#     # num = int("abc") # Это вызовет ValueError
#     my_list = [1, 2]
#     print(my_list[3]) # Это вызовет IndexError
# except ValueError:
#     print("Ошибка преобразования типа данных!")
# except IndexError:
#     print("Ошибка: Индекс выходит за границы списка!")
# except Exception as e: # Общий обработчик для всех остальных исключений
#     print(f"Произошла непредвиденная ошибка: {e}")
#
# # Пример 3: Использование else и finally
#
# def divide_numbers(a, b):
#     try:
#         result = a / b
#     except ZeroDivisionError:
#         print("Нельзя делить на ноль!")
#         return None
#     else:
#         print(f"Деление успешно выполнено. Результат: {result}")
#         return result
#     finally:
#         print("Этот блок выполняется всегда (finally).")
#
# print("\n--- Первый вызов (без ошибки) ---")
# divide_numbers(10, 2)
#
# print("\n--- Второй вызов (с ошибкой) ---")
# divide_numbers(10, 0)

# Пример 4: Вызов собственного исключения

def check_age(age):
    if not isinstance(age, (int, float)):
        raise TypeError("Возраст должен быть числом.")
    if age < 0:
        raise ValueError("Возраст не может быть отрицательным.")
    if age < 18:
        print("Вам меньше 18 лет.")
    else:
        print("Вам 18 лет или больше.")

try:
    check_age(25)
    check_age(-5) # Это вызовет ValueError
except (TypeError, ValueError) as e:
    print(f"Ошибка при проверке возраста: {e}")

try:
    check_age("десять") # Это вызовет TypeError
except (TypeError, ValueError) as e:
    print(f"Ошибка при проверке возраста: {e}")