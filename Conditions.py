age = 20
if age >= 18:
    print("I can vote")
else:
    print("I cannot vote")
    
num = 7
if num%2 == 0:
    print("even number")
else:
    print("odd number")
    
marks = 87
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
else:
    print("Fail")
    
num = 29
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both")
    
age = 22
has_license = False
if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("Get a driving license first")
else:
    print("You are too young to drive")
    
a = 15
b = 25
c = 20
if a > b and a > c:
    print(a, "is largest")
elif b > c:
    print(b, "is largest")
else:
    print(c, "is largest")

a = 5
b = 5
c = 5

if a == b == c:
    print("Equilateral")
elif a == b or b == c or a == c:
    print("Isosceles")
else:
    print("Scalene")

num = 7
is_prime = True
for i in range(2, num):
    if num % i == 0:
     is_prime = False
      break
print(is_prime)
        

