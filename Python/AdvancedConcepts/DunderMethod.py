class Employee:
    company = "HP"
    def __init__(self, name, salary):       # This function is called by default when object created
        self.name = name
        self.salary = salary

    def __str__(self):          # It is for the user who is using this program
        return f"The employee name is {self.name} and the salary is {self.salary}"
    
    def __repr__(self):         #It is mostly used by developer to debug
        return f"name: {self.name}\nsalary : {self.salary}"
    
    def __len__(self):
        return len(self.name)
    


e1 = Employee("Dushyant", 89000)
print(e1.name , e1.salary)

print(str(e1))
print(repr(e1))
print(len(e1))