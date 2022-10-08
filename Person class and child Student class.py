import math
x = math.sqrt(640)
print(x)

class Person:
    # define constructor with attributes: length and width 
    def __init__(self, name , age):
        self.name = name
        self.age = age
        
   
    # create display method
    def display(self):
        print("The length of rectangle is: ", self.name)
        print("The width of rectangle is: ", self.age)
        
class Student(Person):
    def __init__(self, name, age):
        Person.__init__(self, name, age)
        #self.height = height
        
     # create display method
    def displayStudent(self):
        print("The name of student is: ", self.name)
        print("The age of student is: ", self.age)
        
student1 = Student("Ana",23)
student1.displayStudent()
