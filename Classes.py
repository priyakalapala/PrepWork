class Employee:
    def __init__(self, basic, bonus):
        self.basic = basic
        self.bonus = bonus
    def get_Total(self):
        return self.basic+self.bonus
emp1 = Employee(5000, 500)
emp2 = Employee(6000, 600)
print(emp1.get_Total())
print(emp2.get_Total())


class Student:
    def __init__(self, marks1, marks2, marks3):
        self.marks1 = marks1
        self.marks2 = marks2
        self.marks3 = marks3
    def get_Total(self):
        return self.marks1+self.marks2+self.marks3
s1 = Student(85, 90, 95)
s2= Student(40, 67, 78)
print(s1.get_Total())
print(s2.get_Total())

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def get_Total(self):
        return self.length*self.width
rect1 = Rectangle(10, 15)
rect2 = Rectangle(20, 40)
print(rect1.get_Total())
print(rect2.get_Total())

class Trip:
    def __init__(self, d1, d2, d3):
        self.d1 = d1
        self.d2 = d2
        self.d3 = d3
    def get_Total(self):
        return self.d1+self.d2+self.d3
trip = Trip(10, 20, 30)
print(trip.get_Total())

class Student:
    def __init__(self, marks):
        self.marks = marks
    def get_Total(self):
        total = 0
        for m in self.marks:
            total = total+m
            return total
s= Student([85, 90, 95])
print(s.get_Total())