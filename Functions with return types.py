def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return "Hi " + priya

def check_even(num: int, name: str) -> bool:
    
    if num % 2 == 0:
        return True
    else:
        return False

result = check_even(8, "Alice")
print(result) 

result = check_even(7, "Bob")
print(result) 


def is_positive(num: int) -> bool:
      return num > 0

print(is_positive(10)) 
print(is_positive(-5)) 

def is_palindrome(word: str) -> bool:
    return word == word[::-1]

print(is_palindrome("madam"))
print(is_palindrome("hello")) 

def even_or_odd(num: int) -> str:
        if num % 2 == 0:
            return Even
        else:
            return Odd

print(even_or_odd(7)) 
print(even_or_odd(12)) 

def is_adult(age: int, name: str) -> bool:
    if age >= 18:
        return True
    else:
        return False
print(is_adult(20, "Alice"))
print(is_adult(16, "Bob"))

def can_vote(age: int) -> bool:
    return age >= 18

print(can_vote(21)) 
print(can_vote(16))

def is_greater_than_100(num: int) -> bool:
    return num > 100

print(is_greater_than_100(150))
print(is_greater_than_100(50))


def get_grade(score: int) -> str:
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 50:
        return "C"
    else:
        return "Fail"

print(get_grade(85)) 
print(get_grade(40))


def measure_temp(temp: int) -> str:
    if temp >= 40:
        return "hot"
    elif temp == 30:
        return "moderate"
    else:
        return "cool"
print(measure_temp(45))
print(measure_temp(32))





        
