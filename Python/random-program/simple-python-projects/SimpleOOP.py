# simple oop
class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age


NameGiven = input("Enter your name: ")
AgeGiven = int(input("Enter your age: "))
row1 = Student(NameGiven, AgeGiven)
# print(row1)
print(f"Name: {row1.name} \nAge: {row1.age}")
