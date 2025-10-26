"""
Клас Student та пов'язані сутності
"""
from .person import Person
from .interfaces import IStudyable


class Student(Person, IStudyable):
    """Клас студента"""
    
    def __init__(self, first_name: str, last_name: str, course: int, 
                 student_id: str, scholarship: float = 0.0, 
                 passport_series: str = "", passport_number: str = ""):
        super().__init__(first_name, last_name)
        self._course = course
        self._student_id = student_id
        self._scholarship = scholarship
        self._passport_series = passport_series
        self._passport_number = passport_number
    
    @property
    def course(self) -> int:
        return self._course
    
    @course.setter
    def course(self, value: int):
        if not self.validate_course(value):
            raise ValueError("Курс повинен бути від 1 до 6")
        self._course = value
    
    @property
    def student_id(self) -> str:
        return self._student_id
    
    @student_id.setter
    def student_id(self, value: str):
        if not self.validate_student_id(value):
            raise ValueError("Неправильний формат студентського квитка")
        self._student_id = value
    
    @property
    def scholarship(self) -> float:
        return self._scholarship
    
    @scholarship.setter
    def scholarship(self, value: float):
        if not self.validate_scholarship(value):
            raise ValueError("Стипендія не може бути від'ємною")
        self._scholarship = value
    
    @property
    def passport_series(self) -> str:
        return self._passport_series
    
    @passport_series.setter
    def passport_series(self, value: str):
        self._passport_series = value
    
    @property
    def passport_number(self) -> str:
        return self._passport_number
    
    @passport_number.setter
    def passport_number(self, value: str):
        self._passport_number = value
    
    @property
    def passport_full(self) -> str:
        return f"{self.passport_series}{self.passport_number}"
    
    def has_scholarship(self) -> bool:
        """Перевіряє, чи отримує студент стипендію"""
        return self.scholarship > 0
    
    def study(self) -> str:
        """Реалізація методу навчання для студента"""
        return f"{self.get_full_name()} навчається в університеті на {self.course} курсі"
    
    def transfer_to_next_course(self) -> str:
        """Переведення студента на наступний курс"""
        if self.course < 6:
            old_course = self.course
            self.course += 1
            return f"{self.get_full_name()} переведений з {old_course} на {self.course} курс"
        else:
            return f"{self.get_full_name()} вже навчається на останньому курсі"
    
    def validate(self) -> bool:
        """Валідація всіх даних студента"""
        return (super().validate() and 
                self.validate_course(self.course) and
                self.validate_student_id(self.student_id) and
                self.validate_scholarship(self.scholarship))
    
    def to_dict(self) -> dict:
        """Конвертація об'єкта в словник для збереження"""
        return {
            "firstname": self.first_name,
            "lastname": self.last_name,
            "course": self.course,
            "studentId": self.student_id,
            "scholarship": self.scholarship,
            "passportSeries": self.passport_series,
            "passportNumber": self.passport_number
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Створення об'єкта з словника"""
        return cls(
            first_name=data["firstname"],
            last_name=data["lastname"],
            course=data["course"],
            student_id=data["studentId"],
            scholarship=data.get("scholarship", 0.0),
            passport_series=data.get("passportSeries", ""),
            passport_number=data.get("passportNumber", "")
        )
    
    def __str__(self) -> str:
        scholarship_info = f", стипендія: {self.scholarship} грн" if self.has_scholarship() else ", без стипендії"
        return (f"Студент {self.get_full_name()}, {self.course} курс, "
                f"квиток: {self.student_id}{scholarship_info}")
    
    def __repr__(self) -> str:
        return (f"Student('{self.first_name}', '{self.last_name}', "
                f"{self.course}, '{self.student_id}', {self.scholarship})")
