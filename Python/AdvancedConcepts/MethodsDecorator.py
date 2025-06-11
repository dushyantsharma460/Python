class Employee:
    company = "Tesla"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    def print_info(self):
        print(f"The employee name is {self.name} and salary is {self.salary}")

    @staticmethod
    def sum(a,b):              # It does not require self it is a normal method 
        return a + b
    
    @classmethod
    def print_company(cls):
        print(cls.company)

    @classmethod
    def change_company(cls, new_company):       # It needs the class variable and you can handle all the class variable by this
        cls.company = new_company

    



e1 = Employee("Dushyant", 92000)
e2 = Employee("Mayank", 85000)

print(Employee.sum(3,4))

Employee.print_company()
e1.change_company("spaceX")
e1.print_company()