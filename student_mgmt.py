class Student:
    def __init__(self, registration_number, name, email):
        self.__registration_number = registration_number
        self.name = name
        self.email = email

    def get_registration_number(self):
        return self.__registration_number

    def update_profile(self, name, email):
        self.name = name
        self.email = email


student = Student("REG101", "John", "john@example.com")

student.update_profile("John Smith", "johnsmith@example.com")

print(student.get_registration_number())
print(student.name)
print(student.email)