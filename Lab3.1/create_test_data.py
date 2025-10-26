"""
Модуль для створення тестових даних
"""

import sys
import os

# Додаємо поточну директорію до шляху для імпорту модулів
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from entities import Student, Postman, Mountaineer, ClimbingLevel
from file_operations import FileManager


def create_test_data():
    """Створення тестових даних для демонстрації"""
    entities = []

    students_data = [
        ("Іван", "Петренко", 4, "КБ123456", 0.0, "СН", "123456"),
        ("Марія", "Коваленко", 4, "КБ234567", 0.0, "СН", "234567"),
        ("Олексій", "Сидоренко", 4, "КБ345678", 0.0, "СН", "345678"),
        ("Анна", "Шевченко", 4, "КБ456789", 2500.0, "СН", "456789"),
        ("Дмитро", "Мельник", 4, "КБ567890", 3000.0, "СН", "567890"),
        ("Катерина", "Бондаренко", 1, "КБ111111", 1500.0, "СН", "111111"),
        ("Віктор", "Кравченко", 2, "КБ222222", 0.0, "СН", "222222"),
        ("Оксана", "Лисенко", 3, "КБ333333", 2000.0, "СН", "333333"),
        ("Андрій", "Гаврилenko", 5, "КБ555555", 3500.0, "СН", "555555"),
        ("Юлія", "Морозенко", 6, "КБ666666", 0.0, "СН", "666666"),
    ]

    for (
        first_name,
        last_name,
        course,
        student_id,
        scholarship,
        pass_series,
        pass_number,
    ) in students_data:
        student = Student(
            first_name,
            last_name,
            course,
            student_id,
            scholarship,
            pass_series,
            pass_number,
        )
        entities.append(student)

    # Поштарі
    postmen_data = [
        ("Володимир", "Нечипоренко", "Центральний", True, "POST001"),
        ("Галина", "Ткаченко", "Північний", False, "POST002"),
        ("Сергій", "Гриценко", "Південний", True, "POST003"),
    ]

    for first_name, last_name, district, has_license, emp_id in postmen_data:
        postman = Postman(first_name, last_name, district, has_license, emp_id)
        entities.append(postman)

    # Альпіністи
    mountaineers_data = [
        ("Тарас", "Карпенко", ClimbingLevel.EXPERT, 15, "MOUNT001"),
        ("Олена", "Верещак", ClimbingLevel.INTERMEDIATE, 5, "MOUNT002"),
        ("Богдан", "Стецьків", ClimbingLevel.BEGINNER, 1, "MOUNT003"),
        ("Ірина", "Горошко", ClimbingLevel.ADVANCED, 8, "MOUNT004"),
    ]

    for first_name, last_name, level, experience, cert_id in mountaineers_data:
        mountaineer = Mountaineer(first_name, last_name, level, experience, cert_id)
        entities.append(mountaineer)

    return entities


def create_sample_file():
    """Створення зразкового файлу з даними"""
    entities = create_test_data()
    file_manager = FileManager()

    file_path = "sample_data.txt"

    if file_manager.write_to_file(file_path, entities):
        print(f"Створено зразковий файл {file_path} з {len(entities)} записами")
        print("\nВміст файлу:")
        print("-" * 50)

        # Читаємо та виводимо вміст файлу
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            print(content)

        # Перевіряємо читання
        loaded_entities = file_manager.read_from_file(file_path)
        print(f"\nПеревірка: завантажено {len(loaded_entities)} записів")

        return file_path
    else:
        print("Помилка створення файлу")
        return None


def demonstrate_task():
    """Демонстрація виконання основного завдання"""
    file_path = create_sample_file()

    if file_path:
        print("\n" + "=" * 60)
        print("ДЕМОНСТРАЦІЯ ОСНОВНОГО ЗАВДАННЯ")
        print("=" * 60)

        from file_operations import StudentDataProcessor

        file_manager = FileManager()
        processor = StudentDataProcessor()

        # Завантажуємо дані
        entities = file_manager.read_from_file(file_path)

        # Виконуємо завдання
        fourth_year_no_scholarship = (
            processor.find_fourth_year_students_without_scholarship(entities)
        )

        print(f"Результат виконання завдання:")
        print(
            f"Кількість студенті 4-го курсу без стипендії: {len(fourth_year_no_scholarship)}"
        )
        print("\nДані студентів:")

        for i, student in enumerate(fourth_year_no_scholarship, 1):
            print(f"{i}. {student}")
            print(f"   Квиток: {student.student_id}")
            print(f"   Паспорт: {student.passport_full}")
            print()


if __name__ == "__main__":
    demonstrate_task()
