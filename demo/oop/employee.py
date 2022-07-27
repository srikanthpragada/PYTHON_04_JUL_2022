class Employee:
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"{self.id} - {self.name} - {self.salary}"

    def set_salary(self, salary):
        self.salary = salary

    def get_salary(self):
        return self.salary


class OverseasEmployee(Employee):
    def __init__(self, id, name, salary, currency):
        super().__init__(id, name, salary)
        self.currency = currency

    def __str__(self):
        return f"{super().__str__()} - {self.currency}"

    def get_currency(self):
        return self.currency


class NightShiftEmployee(Employee):
    def __init__(self, id, name, salary, allowance):
        super().__init__(id, name, salary)
        self.allowance = allowance

    def __str__(self):
        return f"{super().__str__()} - {self.allowance}"

    def get_allowance(self):
        return self.allowance


e = Employee(1, "James", 70000)
e.set_salary(80000)
print(e)
oe = OverseasEmployee(2, "Andy", 3000, "USD")
print(oe)
print(f"{oe.get_salary()} {oe.get_currency()}")
