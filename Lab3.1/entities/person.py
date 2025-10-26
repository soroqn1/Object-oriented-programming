"""
Базовий абстрактний клас Person
"""
from abc import ABC
from .interfaces import IPerson, ValidationMixin


class Person(IPerson, ValidationMixin, ABC):
    """Абстрактний базовий клас для всіх людей"""
    
    def __init__(self, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name
    
    @property
    def first_name(self) -> str:
        return self._first_name
    
    @first_name.setter
    def first_name(self, value: str):
        if not self.validate_name(value):
            raise ValueError("Неправильний формат імені")
        self._first_name = value
    
    @property
    def last_name(self) -> str:
        return self._last_name
    
    @last_name.setter
    def last_name(self, value: str):
        if not self.validate_name(value):
            raise ValueError("Неправильний формат прізвища")
        self._last_name = value
    
    def get_full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def validate(self) -> bool:
        """Базова валідація Person"""
        return (self.validate_name(self.first_name) and 
                self.validate_name(self.last_name))
    
    def __str__(self) -> str:
        return self.get_full_name()
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.first_name}', '{self.last_name}')"
