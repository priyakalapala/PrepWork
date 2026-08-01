class BankAccount:
  def __init__(self, name, account_no, ifsc_code, balance):
    self.name = name
    self.account_no = account_no
    self.ifsc_code = ifsc_code
    self.balance = balance
account1 = BankAccount("Priya", "1234567890", "SBIN0001234", 50000)
print(account1.name)
print(account1.account_no)
print(account1.ifsc_code)
print(account1.balance)

class student:
    def __init__(self, name, num):
        self.name = name
        self.num = num
s1 = student("priya", 18)
s2 = student("kartheek", 20)
print(s1.name)
print(s2.num)


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
rect1 = Rectangle(10, 5)
print(rect1.length)
print(rect1.width)

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
p1 = person("priya", 30)
p2 = person("kartheek", 32)
print(p1.name)
print(p2.age)

class car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed
c1 = car("Honda", 100)
c2 = car("kia", 120)
print(c1.speed)
print(c2.brand)

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
l1= Laptop("dell", 400)
l2= Laptop("Lenovo", 600)
print(l1.price)
print(l2.brand)

