class Animal:        #Parent class(superclass)
    location= "Africa"
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Speaking now ....")


class Dog(Animal):      # This is how inheritance is done in Python
    def speak(self):
        super().speak()        #Use speak function of the parent class
        print("Barking Sound ...")

a = Animal("Dog")
a.speak()
d = Dog("Bruno")
d.speak()

print(d.location)
print(a.location)
