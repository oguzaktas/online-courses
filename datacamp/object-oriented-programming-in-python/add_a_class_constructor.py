class Employee:
    # Create __init__() method
    def __init__(self, name, hire_date, salary=0):
        self.name = name
        if salary > 0:
            self.salary = salary
        else:
            self.salary = 0
            print("Invalid salary!")

        # Add the hire_date attribute and set it to today's date
        self.hire_date = datetime.today()


# ...Other methods omitted for brevity ...

emp = Employee("Korel Rossi", -1000)
print(emp.name)
print(emp.salary)