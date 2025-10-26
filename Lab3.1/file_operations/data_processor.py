"""
Класи для обробки та пошуку даних
"""
from typing import List, Dict, Any
from .interfaces import IDataProcessor
from entities import Person, Student, Postman, Mountaineer


class StudentDataProcessor(IDataProcessor):
    """Процесор для обробки даних студентів"""
    
    def process_data(self, entities: List[Person]) -> Any:
        """Основна обробка даних для завдання"""
        return self.find_fourth_year_students_without_scholarship(entities)
    
    def find_fourth_year_students_without_scholarship(self, entities: List[Person]) -> List[Student]:
        """Знаходить студентів 4-го курсу без стипендії"""
        result = []
        
        for entity in entities:
            if isinstance(entity, Student):
                if entity.course == 4 and not entity.has_scholarship():
                    result.append(entity)
        
        return result
    
    def count_students_by_course(self, entities: List[Person]) -> Dict[int, int]:
        """Підраховує кількість студентів по курсах"""
        course_count = {}
        
        for entity in entities:
            if isinstance(entity, Student):
                course = entity.course
                course_count[course] = course_count.get(course, 0) + 1
        
        return course_count
    
    def find_students_with_scholarship(self, entities: List[Person]) -> List[Student]:
        """Знаходить студентів, які отримують стипендію"""
        result = []
        
        for entity in entities:
            if isinstance(entity, Student) and entity.has_scholarship():
                result.append(entity)
        
        return result
    
    def get_average_scholarship(self, entities: List[Person]) -> float:
        """Обчислює середню стипендію серед студентів"""
        total_scholarship = 0
        student_count = 0
        
        for entity in entities:
            if isinstance(entity, Student):
                total_scholarship += entity.scholarship
                student_count += 1
        
        return total_scholarship / student_count if student_count > 0 else 0


class PersonSearcher:
    """Клас для пошуку людей за різними критеріями"""
    
    @staticmethod
    def find_by_last_name(entities: List[Person], last_name: str) -> List[Person]:
        """Пошук за прізвищем"""
        result = []
        
        for entity in entities:
            if entity.last_name.lower() == last_name.lower():
                result.append(entity)
        
        return result
    
    @staticmethod
    def find_student_by_id(entities: List[Person], student_id: str) -> Student:
        """Пошук студента за номером студентського квитка"""
        for entity in entities:
            if isinstance(entity, Student) and entity.student_id == student_id:
                return entity
        return None
    
    @staticmethod
    def find_by_full_name(entities: List[Person], first_name: str, last_name: str) -> List[Person]:
        """Пошук за повним іменем"""
        result = []
        
        for entity in entities:
            if (entity.first_name.lower() == first_name.lower() and 
                entity.last_name.lower() == last_name.lower()):
                result.append(entity)
        
        return result


class DataStatistics:
    """Клас для отримання статистики по даних"""
    
    @staticmethod
    def get_entity_count_by_type(entities: List[Person]) -> Dict[str, int]:
        """Отримує кількість сутностей по типах"""
        type_count = {}
        
        for entity in entities:
            entity_type = entity.__class__.__name__
            type_count[entity_type] = type_count.get(entity_type, 0) + 1
        
        return type_count
    
    @staticmethod
    def get_total_count(entities: List[Person]) -> int:
        """Отримує загальну кількість сутностей"""
        return len(entities)
