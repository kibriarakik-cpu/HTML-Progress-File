class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
grade = "10th"
print("Hello, my name is", Student("Alice", 15).name, "and I am in", grade, "grade.")
ob = Student()