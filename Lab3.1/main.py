"""
Лабораторна робота 3.1 - Варіант 14
Моделювання бази даних студентів
Сорочан Ярослав Сергівич
Група ФКНТ Б-121-24-3-ПІ
"""

import json

class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Student(Person):
    def __init__(self, first_name, last_name, course, student_id, scholarship, passport):
        super().__init__(first_name, last_name)
        self.course = course
        self.student_id = student_id
        self.scholarship = scholarship
        self.passport = passport
    
    def study(self):
        print(f"{self.first_name} {self.last_name} навчається на {self.course} курсі")
    
    def __str__(self):
        return (f"Student {self.first_name}{self.last_name}\n"
                f'{{ "firstname": "{self.first_name}", "lastname": "{self.last_name}", '
                f'"course": "{self.course}", "studentId": "{self.student_id}", '
                f'"scholarship": "{self.scholarship}", "passport": "{self.passport}" }};')
    
class Postman(Person):
    def work(self):
        print(f"{self.first_name} {self.last_name} розносить пошту")
    
    def draw(self):
        print(f"{self.first_name} {self.last_name} вміє малювати")


class Mountaineer(Person):
    def work(self):
        print(f"{self.first_name} {self.last_name} підкорює гори")
    
    def draw(self):
        print(f"{self.first_name} {self.last_name} вміє малювати")


class FileManager:
    @staticmethod
    def save_students(students, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for student in students:
                f.write(str(student) + '\n\n')
        print(f"Збережено {len(students)} студентів у файл {filename}")
    
    @staticmethod
    def load_students(filename):
        students = []
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
                blocks = content.strip().split('\n\n')
                
                for block in blocks:
                    if not block.strip():
                        continue
                    
                    lines = block.split('\n')
                    if len(lines) < 2:
                        continue

                    data_line = lines[1].strip() #parsing
                    if data_line.startswith('{') and data_line.endswith('};'):
                        json_str = data_line[:-1]
                        data = json.loads(json_str)
                        
                        student = Student(
                            first_name=data['firstname'],
                            last_name=data['lastname'],
                            course=int(data['course']),
                            student_id=data['studentId'],
                            scholarship=float(data['scholarship']),
                            passport=data['passport']
                        )
                        students.append(student)
            
            print(f"Зчитано {len(students)} студентів з файлу {filename}")
            return students
        
        except FileNotFoundError:
            print(f"Файл {filename} не знайдено")
            return []
        except Exception as e:
            print(f"Помилка при читанні файлу: {e}")
            return []


class StudentDatabase:
    def __init__(self):
        self.students = []
    
    def add_student(self, student):
        self.students.append(student)
    
    def find_by_lastname(self, lastname):
        for student in self.students:
            if student.last_name == lastname:
                return student
        return None
    
    def find_by_student_id(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def count_4th_course_without_scholarship(self):
        count = 0
        result_students = []
        
        for student in self.students:
            if student.course == 4 and student.scholarship == 0:
                count += 1
                result_students.append(student)
        
        return count, result_students
    
    def save_to_file(self, filename):
        FileManager.save_students(self.students, filename)
    
    def load_from_file(self, filename):
        self.students = FileManager.load_students(filename)


def main():
    print("Зчитування студентів з файлу...")
    db = StudentDatabase()
    db.load_from_file("sample_data.txt")
    print()
    
    print("Всі студенти у базі:")
    print("-" * 60)
    for i, student in enumerate(db.students, 1):
        print(f"{i}. {student.last_name} {student.first_name} - Курс {student.course}, Стипендія: {student.scholarship} грн")
    print()
    
    print("Пошук студентів 4-го курсу без стипендії...")
    print("-" * 60)
    
    count, students = db.count_4th_course_without_scholarship()
    
    print(f"\nРЕЗУЛЬТАТ: {count} студентів 4-го курсу не отримують стипендію\n")
    
    if students:
        print("Список студентів:")
        print("-" * 60)
        for i, student in enumerate(students, 1):
            print(f"{i}. {student.last_name} {student.first_name}")
            print(f"Курс: {student.course}")
            print(f"Студентський квиток: {student.student_id}")
            print(f"Паспорт: {student.passport}")
            print(f"Стипендія: {student.scholarship} грн")
            print()
    
    print("=" * 60)
    
    print("\nДемонстрація інших класів:\n")
    
    postman = Postman("Василь", "Іваненко")
    postman.work()
    postman.draw()
    
    mountaineer = Mountaineer("Ольга", "Гірська")
    mountaineer.work()
    mountaineer.draw()
    
    print("\n" + "=" * 60)
    print("Програма завершена успішно!")
    print("=" * 60)


if __name__ == "__main__":
    main()
