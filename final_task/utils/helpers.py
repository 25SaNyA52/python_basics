#Вспомогательные функции для безопасного ввода данных

def get_valid_float(prompt):
    # Безопасно запрашивает у пользователя число с плавающей точкой.
    #
    # Args:
    #     prompt (str): текст приглашения для ввода
    # Returns:
    #     float: корректно введенное число
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Invalid input format. Please enter a number.")


def get_valid_index(prompt, max_index):
    # Безопасно запрашивает у пользователя индекс элемента из списка.
    # Args:
    #     prompt (str): текст приглашения для ввода
    #     max_index (int): максимально допустимый номер (длина списка)
    # Returns:
    #     int: индекс в формате 0-based (начиная с 0)
    while True:
        try:
            value = int(input(prompt))

            # Проверка диапазона (пользователь вводит от 1)
            if 1 <= value <= max_index:
                return value - 1  # Преобразуем в 0-based индекс
            else:
                print(f"Error: Please enter a number between 1 and {max_index}.")
        except ValueError:
            print("Error: Invalid input. Please enter an integer number.")