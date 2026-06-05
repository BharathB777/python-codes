from abc import ABC, abstractmethod

class Patient:
    def __init__(self, name, medical_record):
        self.name = name
        self.__medical_record = medical_record

    def get_medical_record(self):
        return self.__medical_record


class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id


class Doctor(Employee):
    def calculate_salary(self):
        return 100000


class Nurse(Employee):
    def calculate_salary(self):
        return 50000


class Database(ABC):
    @abstractmethod
    def save_data(self):
        pass


class HospitalDatabase(Database):
    def save_data(self):
        print("Data saved to database")


doctor = Doctor("Dr. Smith", 101)
nurse = Nurse("Mary", 102)

print(doctor.calculate_salary())
print(nurse.calculate_salary())