#Главная программа - менеджер геометрических фигур

from shapes import Circle, Rectangle, Triangle  # Абсолютный импорт (без точки!)
from utils import get_valid_float, get_valid_index  # Абсолютный импорт (без точки!)


def main():
    #Главная функция программы с интерактивным меню
    shapes_db = []  # База данных всех фигур

    while True:
        # Основное меню
        print("\n--- SHAPES MANAGER V3.0 ---")
        print("1. Add new shape")
        print("2. List all shapes")
        print("3. Show shape details")
        print("4. Remove shape")
        print("5. Show sum of all areas")
        print("6. Show sum of all perimeters")
        print("7. Exit")

        choice = input("\nChoose an option: ")

        # Опция 1: Добавление новой фигуры
        if choice == '1':
            print("\n--- ADD NEW SHAPE ---")
            print("Types: 1. Circle, 2. Rectangle, 3. Triangle")

            shape_type = input("Select type: ")

            if shape_type not in ['1', '2', '3']:
                print("Error: Invalid shape type!")
                continue

            color = input("Enter color: ")

            try:
                if shape_type == '1':  # Круг
                    radius = get_valid_float("Enter radius: ")
                    shape = Circle(color, radius)

                elif shape_type == '2':  # Прямоугольник
                    width = get_valid_float("Enter width: ")
                    height = get_valid_float("Enter height: ")
                    shape = Rectangle(color, width, height)

                else:  # Треугольник
                    a = get_valid_float("Side A: ")
                    b = get_valid_float("Side B: ")
                    c = get_valid_float("Side C: ")
                    shape = Triangle(color, a, b, c)

                shapes_db.append(shape)
                print("Success: Shape added!")

            except ValueError as e:
                print(f"Logic Error: {e}")

        # Опция 2: Список всех фигур
        elif choice == '2':
            print("\n--- ALL SHAPES ---")

            if not shapes_db:
                print("List is empty.")
            else:
                for i, shape in enumerate(shapes_db, 1):
                    print(f"{i}. {shape}")

        # Опция 3: Детали фигуры
        elif choice == '3':
            print("\n--- SHAPE DETAILS ---")

            if not shapes_db:
                print("List is empty.")
                continue

            idx = get_valid_index(f"Enter shape number (1-{len(shapes_db)}): ", len(shapes_db))
            shape = shapes_db[idx]

            print("-" * 30)
            print(f"Info:      {shape}")
            print(f"Area:      {shape.get_area():.2f}")
            print(f"Perimeter: {shape.get_perimeter():.2f}")
            print("-" * 30)

        # Опция 4: Удаление фигуры
        elif choice == '4':
            print("\n--- REMOVE SHAPE ---")

            if not shapes_db:
                print("List is empty.")
                continue

            idx = get_valid_index(f"Enter shape number to remove (1-{len(shapes_db)}): ", len(shapes_db))
            removed_shape = shapes_db.pop(idx)

            print(f"Success: Removed {removed_shape}")

        # Опция 5: Сумма площадей
        elif choice == '5':
            print("\n--- SUM OF AREAS ---")

            if not shapes_db:
                print("No shapes to calculate.")
            else:
                total_area = sum(shape.get_area() for shape in shapes_db)
                print(f"Total Area of {len(shapes_db)} shapes: {total_area:.2f}")

        # Опция 6: Сумма периметров
        elif choice == '6':
            print("\n--- SUM OF PERIMETERS ---")

            if not shapes_db:
                print("No shapes to calculate.")
            else:
                total_perimeter = sum(shape.get_perimeter() for shape in shapes_db)
                print(f"Total Perimeter of {len(shapes_db)} shapes: {total_perimeter:.2f}")

        # Опция 7: Выход
        elif choice == '7':
            print("\nGoodbye!")
            break

        # Неверный выбор
        else:
            print("Invalid option. Try again.")


# Точка входа программы
if __name__ == "__main__":
    main()