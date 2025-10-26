"""
Інтерфейси для роботи з файлами
"""
from abc import ABC, abstractmethod
from typing import List, Dict, Any, Union
from entities import Person, Student, Postman, Mountaineer


class IFileReader(ABC):
    """Інтерфейс для читання даних з файлу"""
    
    @abstractmethod
    def read_from_file(self, file_path: str) -> List[Person]:
        pass


class IFileWriter(ABC):
    """Інтерфейс для запису даних у файл"""
    
    @abstractmethod
    def write_to_file(self, file_path: str, entities: List[Person]) -> bool:
        pass


class IDataProcessor(ABC):
    """Інтерфейс для обробки даних"""
    
    @abstractmethod
    def process_data(self, entities: List[Person]) -> Any:
        pass
