"""
Клас для роботи з консольним інтерфейсом
"""

from typing import List, Optional, Callable
import sys
from entities import Student, Postman, Mountaineer, ClimbingLevel, ValidationMixin
from file_operations import (
    FileManager,
    StudentDataProcessor,
    PersonSearcher,
    DataStatistics,
)


class ConsoleMenu:
    def __init__(self):
        self.file_manager = FileManager()
        self.data_processor = StudentDataProcessor()
        self.searcher = PersonSearcher()
        self.statistics = DataStatistics()
        self.current_data = []
        self.current_file = "data.txt"

    def show_main_menu(self):
        """Показати головне меню"""
        while True:
            print("\n" + "=" * 50)
            print("СИСТЕМА УПРАВЛІННЯ БАЗОЮ ДАНИХ ЛЮДЕЙ")
            print("=" * 50)
            print("1. Робота з файлами")
            print("2. Управління даними")
            print("3. Пошук та фільтрація")
            print("4. Виконання завдання (студенти 4 курсу без стипендії)")
            print("5. Статистика")
            print("0. Вихід")
            print("-" * 50)

            choice = input("Виберіть опцію: ").strip()

            if choice == "1":
                self.file_menu()
            elif choice == "2":
                self.data_management_menu()
            elif choice == "3":
                self.search_menu()
            elif choice == "4":
                self.execute_main_task()
            elif choice == "5":
                self.show_statistics()
            elif choice == "0":
                print("До побачення!")
                sys.exit(0)
            else:
                print("Неправильний вибір. Спробуйте ще раз.")

    def file_menu(self):
        """Меню роботи з файлами"""
        while True:
            print("\n" + "-" * 30)
            print("РОБОТА З ФАЙЛАМИ")
            print("-" * 30)
            print("1. Завантажити дані з файлу")
            print("2. Зберегти дані у файл")
            print("3. Створити новий файл")
            print("4. Показати поточний файл")
            print("0. Назад до головного меню")

            choice = input("Виберіть опцію: ").strip()

            if choice == "1":
                self.load_from_file()
            elif choice == "2":
                self.save_to_file()
            elif choice == "3":
                self.create_new_file()
            elif choice == "4":
                print(f"Поточний файл: {self.current_file}")
            elif choice == "0":
                break
            else:
                print("Неправильний вибір.")

    def data_management_menu(self):
        """Меню управління даними"""
        while True:
            print("\n" + "-" * 30)
            print("УПРАВЛІННЯ ДАНИМИ")
            print("-" * 30)
            print("1. Додати студента")
            print("2. Додати поштаря")
            print("3. Додати альпініста")
            print("4. Показати всі дані")
            print("5. Видалити особу")
            print("0. Назад до головного меню")

            choice = input("Виберіть опцію: ").strip()

            if choice == "1":
                self.add_student()
            elif choice == "2":
                self.add_postman()
            elif choice == "3":
                self.add_mountaineer()
            elif choice == "4":
                self.show_all_data()
            elif choice == "5":
                self.delete_person()
            elif choice == "0":
                break
            else:
                print("Неправильний вибір.")

    def search_menu(self):
        """Меню пошуку"""
        while True:
            print("\n" + "-" * 30)
            print("ПОШУК ТА ФІЛЬТРАЦІЯ")
            print("-" * 30)
            print("1. Пошук за прізвищем")
            print("2. Пошук студента за номером квитка")
            print("3. Пошук за повним іменем")
            print("4. Показати всіх студентів")
            print("5. Показати студентів зі стипендією")
            print("0. Назад до головного меню")

            choice = input("Виберіть опцію: ").strip()

            if choice == "1":
                self.search_by_last_name()
            elif choice == "2":
                self.search_student_by_id()
            elif choice == "3":
                self.search_by_full_name()
            elif choice == "4":
                self.show_all_students()
            elif choice == "5":
                self.show_students_with_scholarship()
            elif choice == "0":
                break
            else:
                print("Неправильний вибір.")

    def load_from_file(self):
        """Завантаження даних з файлу"""
        file_path = input("Введіть шлях до файлу (або Enter для поточного): ").strip()
        if not file_path:
            file_path = self.current_file

        try:
            self.current_data = self.file_manager.read_from_file(file_path)
            self.current_file = file_path
            print(f"Завантажено {len(self.current_data)} записів з файлу {file_path}")
        except Exception as e:
            print(f"Помилка завантаження: {e}")

    def save_to_file(self):
        """Збереження даних у файл"""
        if not self.current_data:
            print("Немає даних для збереження. Спочатку додайте дані.")
            return

        file_path = input("Введіть шлях до файлу (або Enter для поточного): ").strip()
        if not file_path:
            file_path = self.current_file

        if self.file_manager.write_to_file(file_path, self.current_data):
            self.current_file = file_path
            print(f"Дані збережено у файл {file_path}")
        else:
            print("Помилка збереження даних")

    def create_new_file(self):
        """Створення нового файлу"""
        file_path = input("Введіть шлях до нового файлу: ").strip()
        if self.file_manager.create_empty_file(file_path):
            self.current_file = file_path
            self.current_data = []
            print(f"Створено новий файл {file_path}")
        else:
            print("Помилка створення файлу")

    def add_student(self):
        """Додавання студента"""
        print("\nДодавання студента:")

        try:
            first_name = self.input_with_validation(
                "Ім'я: ", ValidationMixin.validate_name
            )
            last_name = self.input_with_validation(
                "Прізвище: ", ValidationMixin.validate_name
            )

            course = int(input("Курс (1-6): "))
            if not ValidationMixin.validate_course(course):
                print("Неправильний курс")
                return

            student_id = self.input_with_validation(
                "Студентський квиток (формат КБ123456): ",
                ValidationMixin.validate_student_id,
            )

            scholarship = float(input("Стипендія (0 якщо немає): "))
            if not ValidationMixin.validate_scholarship(scholarship):
                print("Неправильна стипендія")
                return

            passport_series = input("Серія паспорту (необов'язково): ").strip()
            passport_number = input("Номер паспорту (необов'язково): ").strip()

            student = Student(
                first_name,
                last_name,
                course,
                student_id,
                scholarship,
                passport_series,
                passport_number,
            )

            if student.validate():
                self.current_data.append(student)
                print(f"Студента {student} додано успішно")

                # Демонстрація методів
                print(f"Інформація про навчання: {student.study()}")

            else:
                print("Помилка валідації даних студента")

        except ValueError as e:
            print(f"Помилка введення: {e}")
        except Exception as e:
            print(f"Помилка: {e}")

    def add_postman(self):
        """Додавання поштаря"""
        print("\nДодавання поштаря:")

        try:
            first_name = self.input_with_validation(
                "Ім'я: ", ValidationMixin.validate_name
            )
            last_name = self.input_with_validation(
                "Прізвище: ", ValidationMixin.validate_name
            )

            work_district = input("Робочий район (необов'язково): ").strip()

            has_license = input("Має водійські права? (y/n): ").strip().lower() == "y"
            employee_id = input("ID співробітника (необов'язково): ").strip()

            postman = Postman(
                first_name, last_name, work_district, has_license, employee_id
            )

            if postman.validate():
                self.current_data.append(postman)
                print(f"Поштаря {postman} додано успішно")

                # Демонстрація методів
                print(f"Інформація про роботу: {postman.work()}")
                print(f"Інформація про керування: {postman.drive()}")

            else:
                print("Помилка валідації даних поштаря")

        except Exception as e:
            print(f"Помилка: {e}")

    def add_mountaineer(self):
        """Додавання альпініста"""
        print("\nДодавання альпініста:")

        try:
            first_name = self.input_with_validation(
                "Ім'я: ", ValidationMixin.validate_name
            )
            last_name = self.input_with_validation(
                "Прізвище: ", ValidationMixin.validate_name
            )

            print("Рівні підготовки:")
            for i, level in enumerate(ClimbingLevel, 1):
                print(f"{i}. {level.value}")

            level_choice = int(input("Виберіть рівень (1-4): "))
            levels = list(ClimbingLevel)
            if 1 <= level_choice <= len(levels):
                climbing_level = levels[level_choice - 1]
            else:
                print("Неправильний вибір рівня")
                return

            years_experience = int(input("Років досвіду: "))
            if years_experience < 0:
                print("Досвід не може бути від'ємним")
                return

            cert_id = input("ID сертифікації (необов'язково): ").strip()

            mountaineer = Mountaineer(
                first_name, last_name, climbing_level, years_experience, cert_id
            )

            if mountaineer.validate():
                self.current_data.append(mountaineer)
                print(f"Альпініста {mountaineer} додано успішно")

                # Демонстрація методів
                print(f"Інформація про навчання: {mountaineer.study()}")
                print(f"Інформація про сходження: {mountaineer.climb()}")

            else:
                print("Помилка валідації даних альпініста")

        except ValueError as e:
            print(f"Помилка введення: {e}")
        except Exception as e:
            print(f"Помилка: {e}")

    def show_all_data(self):
        """Показати всі дані"""
        if not self.current_data:
            print("Немає даних для відображення")
            return

        print(f"\nВсього записів: {len(self.current_data)}")
        print("-" * 60)

        for i, entity in enumerate(self.current_data, 1):
            print(f"{i}. {entity}")

    def execute_main_task(self):
        """Виконання основного завдання - знайти студентів 4 курсу без стипендії"""
        if not self.current_data:
            print("Немає даних для обробки. Завантажте дані з файлу.")
            return

        print("\n" + "=" * 50)
        print("ВИКОНАННЯ ОСНОВНОГО ЗАВДАННЯ")
        print("Пошук студентів 4-го курсу без стипендії")
        print("=" * 50)

        result = self.data_processor.find_fourth_year_students_without_scholarship(
            self.current_data
        )

        if result:
            print(f"Знайдено {len(result)} студентів 4-го курсу без стипендії:")
            print("-" * 60)

            for i, student in enumerate(result, 1):
                print(f"{i}. {student}")
                print(f"   Квиток: {student.student_id}")
                if student.passport_full:
                    print(f"   Паспорт: {student.passport_full}")
                print()
        else:
            print("Студентів 4-го курсу без стипендії не знайдено")

        # Додаткова статистика
        all_students = [
            entity for entity in self.current_data if isinstance(entity, Student)
        ]
        fourth_year_students = [s for s in all_students if s.course == 4]

        print(f"Додаткова інформація:")
        print(f"- Всього студентів: {len(all_students)}")
        print(f"- Студентів 4-го курсу: {len(fourth_year_students)}")
        print(f"- Студентів 4-го курсу без стипендії: {len(result)}")

    def show_statistics(self):
        """Показати статистику"""
        if not self.current_data:
            print("Немає даних для статистики")
            return

        print("\n" + "=" * 40)
        print("СТАТИСТИКА")
        print("=" * 40)

        # Загальна статистика
        type_count = self.statistics.get_entity_count_by_type(self.current_data)
        total = self.statistics.get_total_count(self.current_data)

        print(f"Загальна кількість записів: {total}")
        print("\nПо типах:")
        for entity_type, count in type_count.items():
            print(f"- {entity_type}: {count}")

        # Статистика по студентах
        course_count = self.data_processor.count_students_by_course(self.current_data)
        if course_count:
            print("\nСтуденти по курсах:")
            for course in sorted(course_count.keys()):
                print(f"- {course} курс: {course_count[course]} студентів")

        # Середня стипендія
        avg_scholarship = self.data_processor.get_average_scholarship(self.current_data)
        if avg_scholarship > 0:
            print(f"\nСередня стипендія: {avg_scholarship:.2f} грн")

    def search_by_last_name(self):
        """Пошук за прізвищем"""
        if not self.current_data:
            print("Немає даних для пошуку")
            return

        last_name = input("Введіть прізвище: ").strip()
        results = self.searcher.find_by_last_name(self.current_data, last_name)

        if results:
            print(f"Знайдено {len(results)} записів:")
            for i, person in enumerate(results, 1):
                print(f"{i}. {person}")
        else:
            print(f"Особи з прізвищем '{last_name}' не знайдено")

    def search_student_by_id(self):
        """Пошук студента за ID"""
        if not self.current_data:
            print("Немає даних для пошуку")
            return

        student_id = input("Введіть номер студентського квитка: ").strip()
        student = self.searcher.find_student_by_id(self.current_data, student_id)

        if student:
            print(f"Знайдено студента: {student}")
        else:
            print(f"Студента з квитком '{student_id}' не знайдено")

    def search_by_full_name(self):
        """Пошук за повним іменем"""
        if not self.current_data:
            print("Немає даних для пошуку")
            return

        first_name = input("Введіть ім'я: ").strip()
        last_name = input("Введіть прізвище: ").strip()

        results = self.searcher.find_by_full_name(
            self.current_data, first_name, last_name
        )

        if results:
            print(f"Знайдено {len(results)} записів:")
            for i, person in enumerate(results, 1):
                print(f"{i}. {person}")
        else:
            print(f"Особи з іменем '{first_name} {last_name}' не знайдено")

    def show_all_students(self):
        """Показати всіх студентів"""
        students = [
            entity for entity in self.current_data if isinstance(entity, Student)
        ]

        if students:
            print(f"Всього студентів: {len(students)}")
            print("-" * 50)
            for i, student in enumerate(students, 1):
                print(f"{i}. {student}")
        else:
            print("Студентів не знайдено")

    def show_students_with_scholarship(self):
        """Показати студентів зі стипендією"""
        students = self.data_processor.find_students_with_scholarship(self.current_data)

        if students:
            print(f"Студентів зі стипендією: {len(students)}")
            print("-" * 50)
            for i, student in enumerate(students, 1):
                print(f"{i}. {student}")
        else:
            print("Студентів зі стипендією не знайдено")

    def delete_person(self):
        """Видалення особи"""
        if not self.current_data:
            print("Немає даних для видалення")
            return

        self.show_all_data()

        try:
            index = int(input("Введіть номер для видалення: ")) - 1
            if 0 <= index < len(self.current_data):
                deleted = self.current_data.pop(index)
                print(f"Видалено: {deleted}")
            else:
                print("Неправильний номер")
        except ValueError:
            print("Введіть число")

    def input_with_validation(
        self, prompt: str, validator: Callable[[str], bool]
    ) -> str:
        """Введення з валідацією"""
        while True:
            value = input(prompt).strip()
            if validator(value):
                return value
            else:
                print("Неправильний формат. Спробуйте ще раз.")
