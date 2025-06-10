class Employee:
    company = "Asus"

    def __init__(self, salary, name, bond, company):
        self.salary = salary
        self.name = name 
        self.bond = bond
        self.company = company

    def getSalary(self):
        return self.salary
    
    def getInfo(self):
        print(f"{self.name}! you have bond of {self.bond} with the base salary {self.salary}")


e1 = Employee(44000, "Rohit", 4, "Tesla")

print(e1.company)           #Will print instance attribute whenever it is present if not then print class attribute
print(Employee.company)        #This will always print the class Attribute 


#Object introspection
print(dir(e1))          #Print all the method and the variable which is associated to object e1