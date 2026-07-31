def function_name():
    print("Hello,python!")
function_name()

def greet(name):
    print("Hello", name)
greet("priya")

def add(a, b):
    return a+b
result = add(3, 5)
print(result)

def multiply(a, b):
    return a*b
result = multiply(3, 5)
print(result)

print(len("python"))

def square(n):
    return n*n
print(square(6))

def is_even(num):
    if num%2==0:
        return True
    else:
        return False
print(is_even(10))
print(is_even(7))


def print_numbers(n):
    for i in range(1, n):
        print(i)
print_numbers(5)

def max_num(a, b):
    if a>b:
        return a
    else:
        return b
print(max_num(10, 20))

def simple_interest(p, t, r):
    return(p*t*r)/100
print(simple_interest(1000, 2, 5))

def divide(a, b):
    return a/b
result = divide(20,3)
print(result)

def get_location(location_id):
    return location_id
result = get_location(85254)
print(result)

def check_age(age):
    if age>= 18:
        return "Adult"
    else:
        return "Minor"
print(check_age(20))

def find_max(numbers):
    return max(numbers)
print(find_max([10, 20, 30, 40]))

def is_positive(num):
    return num>0
print (is_positive(10))
print(is_positive(-5))