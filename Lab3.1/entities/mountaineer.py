"""
Клас Mountaineer (Альпініст)
"""
from .person import Person
from .interfaces import IStudyable
from enum import Enum


class ClimbingLevel(Enum):
    """Рівні альпіністської підготовки"""
    BEGINNER = "початківець"
    INTERMEDIATE = "середній"
    ADVANCED = "просунутий"
    EXPERT = "експерт"


class Mountaineer(Person, IStudyable):
    """Клас альпініста"""
    
    def __init__(self, first_name: str, last_name: str, 
                 climbing_level: ClimbingLevel = ClimbingLevel.BEGINNER,
                 years_experience: int = 0, certification_id: str = ""):
        super().__init__(first_name, last_name)
        self._climbing_level = climbing_level
        self._years_experience = years_experience
        self._certification_id = certification_id
    
    @property
    def climbing_level(self) -> ClimbingLevel:
        return self._climbing_level
    
    @climbing_level.setter
    def climbing_level(self, value: ClimbingLevel):
        self._climbing_level = value
    
    @property
    def years_experience(self) -> int:
        return self._years_experience
    
    @years_experience.setter
    def years_experience(self, value: int):
        if value < 0:
            raise ValueError("Досвід не може бути від'ємним")
        self._years_experience = value
    
    @property
    def certification_id(self) -> str:
        return self._certification_id
    
    @certification_id.setter
    def certification_id(self, value: str):
        self._certification_id = value
    
    def study(self) -> str:
        """Реалізація методу навчання для альпініста"""
        return f"{self.get_full_name()} вивчає техніки альпінізму та підвищує свою кваліфікацію"
    
    def climb(self) -> str:
        """Специфічний метод сходження"""
        return f"{self.get_full_name()} здійснює альпіністське сходження (рівень: {self.climbing_level.value})"
    
    def train(self) -> str:
        """Тренування альпініста"""
        return f"{self.get_full_name()} тренується для покращення альпіністських навичок"
    
    def upgrade_level(self) -> str:
        """Підвищення рівня майстерності"""
        levels = list(ClimbingLevel)
        current_index = levels.index(self.climbing_level)
        
        if current_index < len(levels) - 1:
            old_level = self.climbing_level.value
            self.climbing_level = levels[current_index + 1]
            return f"{self.get_full_name()} підвищив рівень з '{old_level}' до '{self.climbing_level.value}'"
        else:
            return f"{self.get_full_name()} вже досяг максимального рівня майстерності"
    
    def validate(self) -> bool:
        """Валідація даних альпініста"""
        return (super().validate() and 
                self.years_experience >= 0)
    
    def to_dict(self) -> dict:
        """Конвертація об'єкта в словник для збереження"""
        return {
            "firstname": self.first_name,
            "lastname": self.last_name,
            "climbingLevel": self.climbing_level.value,
            "yearsExperience": self.years_experience,
            "certificationId": self.certification_id
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Створення об'єкта з словника"""
        # Знаходимо рівень за значенням
        level = ClimbingLevel.BEGINNER
        for lvl in ClimbingLevel:
            if lvl.value == data.get("climbingLevel", "початківець"):
                level = lvl
                break
        
        return cls(
            first_name=data["firstname"],
            last_name=data["lastname"],
            climbing_level=level,
            years_experience=data.get("yearsExperience", 0),
            certification_id=data.get("certificationId", "")
        )
    
    def __str__(self) -> str:
        exp_info = f", досвід: {self.years_experience} років" if self.years_experience > 0 else ""
        return f"Альпініст {self.get_full_name()}, рівень: {self.climbing_level.value}{exp_info}"
    
    def __repr__(self) -> str:
        return (f"Mountaineer('{self.first_name}', '{self.last_name}', "
                f"{self.climbing_level}, {self.years_experience})")
