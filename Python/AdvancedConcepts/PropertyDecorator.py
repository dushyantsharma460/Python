class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @property
    def first_name(self):
        new_name = self.name.split(" ")
        return new_name[0]
    
    @first_name.setter
    def first_name(self, new_name):
        name = self.name.split(" ")
        new_string = f"{new_name} {name[1]}"
        self.name = new_string

e = Employee("Dushyant Sharma", 42000)

# print(e.get_first_name())

# e.set_first_name("Mayank")
# print(e.name)

# e.projects = 6 
# print(e.projects)


print(e.first_name)
e.first_name = "Mayank"
print(e.name)
