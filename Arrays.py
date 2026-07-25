numbers =[10, 20, 30]
numbers.append(40)
print(numbers)


numbers = [10, 20, 30]
numbers.insert(1, 15)
print(numbers)

numbers = [10, 20, 30, 40]
numbers.remove(20)
print(numbers)

numbers = [10, 20, 30, 40]
del numbers[2]
print(numbers)

numbers = [10, 20, 30, 40]
print(len(numbers))

numbers = [40, 10, 30, 20]
numbers.sort()
print(numbers)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)

numbers = [10, 45, 23, 89, 12]
numbers.sort()
print(numbers[-2])

numbers = [10, 50, 23, 44, 5]
numbers.sort()
print(numbers[-3])

num = [10, 15, 20, 25, 30]
for i in num:
 if i%2 == 0:
    print("even number")
 else:
    print("odd number")
    
num= [15, 22, 43, 55, 32]
for i in num:
    if num% 2 !=0:
        print("even number")
    