#Is the process of writing a program by use of classes and objects
#Class is a blue print of an Object
#Object us an instance of a class

class Employee:
    name = "Mary"
    gender = "Female"
    position = "Developer"
    def __init__(self, name, gender, position):
        self.name = name
        self.gender = gender
        self.position = position
    def movement(self):
        print(Employee is walking)

 #creating an object
employee1 = Employee("Mary", "Female", "Developer")
employee2 = Employee("john", "Male", "Adm")
