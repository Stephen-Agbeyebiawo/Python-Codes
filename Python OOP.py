class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()
        return value/len(self.students)

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what I say")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) #refers to parent class
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

class Dog(Pet):
    def speak(self):
        print("Bark")

class Person:
    number_of_people = 0    #class attribute

    """
    def __init__(self, name):
        self.name = name
        Person.number_of_people += 1"""    #number_of_people increases whenever a persion object is created

    def __init__(self, name):
        self.name = name
        Person.add_person()
     
    @classmethod
    def number_of_people_(cls):
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

#statis class methods

class Math:
    @staticmethod
    def add5(x):
        return x + 5

    @staticmethod
    def add10(x):
        return x + 10

    @staticmethod
    def pr():
        print("run")

"""   
print(Math.add10(5))
Math.pr()
"""
