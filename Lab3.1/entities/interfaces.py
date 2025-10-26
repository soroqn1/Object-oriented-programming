"""
Інтерфейси та абстракції для сутностей
"""
from abc import ABC, abstractmethod
import re


class IValidatable(ABC):
    """Інтерфейс для валідації даних"""
    
    @abstractmethod
    def validate(self) -> bool:
        pass


class ITeachable(ABC):
    """Інтерфейс для сутностей, які можуть навчати"""
    
    @abstractmethod
    def teach(self) -> str:
        pass


class IStudyable(ABC):
    """Інтерфейс для сутностей, які можуть навчатися"""
    
    @abstractmethod
    def study(self) -> str:
        pass


class IDriveable(ABC):
    """Інтерфейс для сутностей, які можуть керувати транспортом"""
    
    @abstractmethod
    def drive(self) -> str:
        pass


class IWorker(ABC):
    """Інтерфейс для працівників"""
    
    @abstractmethod
    def work(self) -> str:
        pass


class IPerson(IValidatable):
    """Інтерфейс для людини"""
    
    @property
    @abstractmethod
    def first_name(self) -> str:
        pass
    
    @property
    @abstractmethod
    def last_name(self) -> str:
        pass
    
    @abstractmethod
    def get_full_name(self) -> str:
        pass


class ValidationMixin:
    """Mixin клас для валідації даних"""
    
    @staticmethod
    def validate_name(name: str) -> bool:
        """Валідація імені та прізвища"""
        pattern = r'^[А-Яа-яІіЇїЄєA-Za-z\s\'-]{2,50}$'
        return bool(re.match(pattern, name))
    
    @staticmethod
    def validate_student_id(student_id: str) -> bool:
        """Валідація студентського квитка (формат: КБ123456)"""
        pattern = r'^[А-Я]{2}\d{6}$'
        return bool(re.match(pattern, student_id))
    
    @staticmethod
    def validate_passport(passport: str) -> bool:
        """Валідація паспорту (формат: СН123456)"""
        pattern = r'^[А-Я]{2}\d{6}$'
        return bool(re.match(pattern, passport))
    
    @staticmethod
    def validate_course(course: int) -> bool:
        """Валідація курсу (1-6)"""
        return 1 <= course <= 6
    
    @staticmethod
    def validate_scholarship(scholarship: float) -> bool:
        """Валідація стипендії (>= 0)"""
        return scholarship >= 0
