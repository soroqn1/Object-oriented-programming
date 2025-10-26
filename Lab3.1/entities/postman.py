"""
Клас Postman (Поштар)
"""
from .person import Person
from .interfaces import IWorker, IDriveable


class Postman(Person, IWorker, IDriveable):
    """Клас поштаря"""
    
    def __init__(self, first_name: str, last_name: str, work_district: str = "", 
                 has_driving_license: bool = False, employee_id: str = ""):
        super().__init__(first_name, last_name)
        self._work_district = work_district
        self._has_driving_license = has_driving_license
        self._employee_id = employee_id
    
    @property
    def work_district(self) -> str:
        return self._work_district
    
    @work_district.setter
    def work_district(self, value: str):
        self._work_district = value
    
    @property
    def has_driving_license(self) -> bool:
        return self._has_driving_license
    
    @has_driving_license.setter
    def has_driving_license(self, value: bool):
        self._has_driving_license = value
    
    @property
    def employee_id(self) -> str:
        return self._employee_id
    
    @employee_id.setter
    def employee_id(self, value: str):
        self._employee_id = value
    
    def work(self) -> str:
        """Реалізація методу роботи для поштаря"""
        district_info = f" в районі {self.work_district}" if self.work_district else ""
        return f"{self.get_full_name()} працює поштарем{district_info}"
    
    def drive(self) -> str:
        """Реалізація методу керування транспортом"""
        if self.has_driving_license:
            return f"{self.get_full_name()} керує службовим транспортом для доставки пошти"
        else:
            return f"{self.get_full_name()} не має водійських прав"
    
    def deliver_mail(self) -> str:
        """Специфічний метод доставки пошти"""
        return f"{self.get_full_name()} доставляє пошту"
    
    def validate(self) -> bool:
        """Валідація даних поштаря"""
        return super().validate()
    
    def to_dict(self) -> dict:
        """Конвертація об'єкта в словник для збереження"""
        return {
            "firstname": self.first_name,
            "lastname": self.last_name,
            "workDistrict": self.work_district,
            "hasDrivingLicense": self.has_driving_license,
            "employeeId": self.employee_id
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """Створення об'єкта з словника"""
        return cls(
            first_name=data["firstname"],
            last_name=data["lastname"],
            work_district=data.get("workDistrict", ""),
            has_driving_license=data.get("hasDrivingLicense", False),
            employee_id=data.get("employeeId", "")
        )
    
    def __str__(self) -> str:
        license_info = " (з водійськими правами)" if self.has_driving_license else " (без водійських прав)"
        district_info = f", район: {self.work_district}" if self.work_district else ""
        return f"Поштар {self.get_full_name()}{license_info}{district_info}"
    
    def __repr__(self) -> str:
        return (f"Postman('{self.first_name}', '{self.last_name}', "
                f"'{self.work_district}', {self.has_driving_license})")
