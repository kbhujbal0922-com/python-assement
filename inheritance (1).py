class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
    def display(self):
        print(self.name,self.age)

class student(Person):
    def __init__(self,name,age,marks):
        Person.__init__(self,name,age)
        self.marks = marks

    def stud(self):
        print(" I am a student")

stud1 = student("kaushal" , 18 , 96)
stud1. stud()
stud1.marks = 97
stud1.name = "sagar"  
stud1.display()
      


