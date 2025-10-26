"""
Клас для роботи з файлами у специфічному форматі
"""
import json
import re
from typing import List, Dict, Any
from .interfaces import IFileReader, IFileWriter
from entities import Person, Student, Postman, Mountaineer, ClimbingLevel


class FileManager(IFileReader, IFileWriter):
    """Менеджер файлів для читання та запису даних сутностей"""
    
    def __init__(self):
        self._type_mapping = {
            "Student": Student,
            "Postman": Postman,
            "Mountaineer": Mountaineer
        }
    
    def write_to_file(self, file_path: str, entities: List[Person]) -> bool:
        """Запис сутностей у файл у заданому форматі"""
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                for entity in entities:
                    # Запис типу та імені об'єкта
                    object_name = f"{entity.first_name}{entity.last_name}"
                    file.write(f"{entity.__class__.__name__} {object_name}\n")
                    
                    # Запис атрибутів у JSON форматі
                    attributes = entity.to_dict()
                    json_str = json.dumps(attributes, ensure_ascii=False, indent=0)
                    # Прибираємо зайві переноси рядків всередині JSON
                    json_str = json_str.replace('\n', '')
                    file.write(f"{json_str};\n")
            
            return True
        except Exception as e:
            print(f"Помилка при записі у файл: {e}")
            return False
    
    def read_from_file(self, file_path: str) -> List[Person]:
        """Читання сутностей з файлу"""
        entities = []
        
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
                
                # Розбираємо файл по блоках (кожен блок - це тип + JSON)
                pattern = r'(\w+)\s+(\w+)\s*\n(\{[^}]+\});'
                matches = re.findall(pattern, content, re.MULTILINE | re.DOTALL)
                
                for match in matches:
                    entity_type, object_name, json_data = match
                    
                    try:
                        # Парсимо JSON дані
                        data = json.loads(json_data)
                        
                        # Створюємо об'єкт відповідного типу
                        if entity_type in self._type_mapping:
                            entity_class = self._type_mapping[entity_type]
                            entity = entity_class.from_dict(data)
                            entities.append(entity)
                        else:
                            print(f"Невідомий тип сутності: {entity_type}")
                    
                    except json.JSONDecodeError as e:
                        print(f"Помилка парсингу JSON для {entity_type}: {e}")
                    except Exception as e:
                        print(f"Помилка створення об'єкта {entity_type}: {e}")
        
        except FileNotFoundError:
            print(f"Файл {file_path} не знайдено")
        except Exception as e:
            print(f"Помилка при читанні файлу: {e}")
        
        return entities
    
    def append_to_file(self, file_path: str, entity: Person) -> bool:
        """Додавання однієї сутності до файлу"""
        try:
            with open(file_path, 'a', encoding='utf-8') as file:
                object_name = f"{entity.first_name}{entity.last_name}"
                file.write(f"{entity.__class__.__name__} {object_name}\n")
                
                attributes = entity.to_dict()
                json_str = json.dumps(attributes, ensure_ascii=False, indent=0)
                json_str = json_str.replace('\n', '')
                file.write(f"{json_str};\n")
            
            return True
        except Exception as e:
            print(f"Помилка при додаванні до файлу: {e}")
            return False
    
    def create_empty_file(self, file_path: str) -> bool:
        """Створення порожнього файлу"""
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write("")  # Створюємо порожній файл
            return True
        except Exception as e:
            print(f"Помилка при створенні файлу: {e}")
            return False
