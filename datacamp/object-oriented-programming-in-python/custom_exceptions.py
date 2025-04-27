class SalaryError(ValueError): pass


class BonusError(SalaryError): pass


class Employee:
    MIN_SALARY = 30000
    MAX_BONUS = 5000

    def __init__(self, name, salary=30000):
        self.name = name
        if salary < Employee.MIN_SALARY:
            raise SalaryError("Salary is too low!")
        self.salary = salary

    # Rewrite using exceptions
    def give_bonus(self, amount):
        if amount > Employee.MAX_BONUS:
            print("The bonus amount is too high!")
            raise BonusError()
        elif self.salary + amount < Employee.MIN_SALARY:
            print("The salary after bonus is too low!")
            raise SalaryError()
        else:
            self.salary += amount