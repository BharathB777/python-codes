class Employee:
    def __init__(self, name, salary, employee_id):
        self.name = name
        self.salary = salary
        self.employee_id = employee_id


class Manager(Employee):
    def __init__(self, name, salary, employee_id, team_size):
        super().__init__(name, salary, employee_id)
        self.team_size = team_size


class Developer(Employee):
    def __init__(self, name, salary, employee_id, programming_language):
        super().__init__(name, salary, employee_id)
        self.programming_language = programming_language


manager = Manager("Alice", 90000, "M101", 10)
developer = Developer("Bob", 70000, "D101", "Python")

print(manager.name, manager.team_size)
print(developer.name, developer.programming_language)