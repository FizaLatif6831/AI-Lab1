#ask user their name and age, and print greeting
"""
name= input("enter you name: ")
age = input("enter your age: ")
print("hello", name, "!! aged", age)
"""

#data identification

"""
value = input("Enter a value: ")
try:
    value = int(value)
except:
    try:
      value = float(value)
    except:
      value = str(value)
print(type(value))
"""

#list
"""
list_of_elements=[]

size=int(input("enter the size of list:"))

for i in range(size):
    element= input("enter an element in the list:")
    list_of_elements.append(element)  #modifying tuple

s2 = [s.upper() for s in list_of_elements]
print("printing the list in all upper case", s2)

remove_element= input("enter the element you want to remove:")
list_of_elements.remove(remove_element)

s2 = [s.upper() for s in list_of_elements]
print("after removing the speciifed element, the list will be:", s2)
"""

#unpacking tuples
"""
fruits = {"apple","mango"} #making tuple
(red,yellow)=fruits #unpacking tuple

print(red)
print(yellow)
"""

#dictionary 

"""
dict1 = {"x1": 'A', "x2": 'A+', "x3": 'B', "x4": 'B+', "x5": 'B-'}
print(dict1)
"""

#taking 2 lists as inputs and converting them into list and perform operations
"""
list1=[]
list2=[]
size=int(input('enter the number of elements:'))

for i in range(size):
    element=input(f"enter element {i+1} for list 1:")
    list1.append(element)

print('List 1:',list1)

for i in range(size):
    element2=input(f"enter element {i+1} for list 2: ")
    list2.append(element2)

print('List 2:',list2)

#converting the lists to sets
set1= set(list1)
set2= set(list2)

#printing union
print("the union of the two sets is", set1.union(set2))

#printing intersection
print("the intersection of the two sets is", set1.intersection(set2))

#printing difference
print("the difference of the two sets is", set1.difference(set2))
"""

#number checker
"""
number= int(input("please enter a number: "))
if number>0:
    if number%2==0:
     print("number is positive AND an even number")
    else:
       print("number is a positive and odd number")
elif number<0:
    if number%2==0:
        print("number is negative AND an even number")
    else:
       print("number is negative AND odd")
else:
    print("number is zero.")
"""

#printing 1 to 50 (fizzbuzz)
"""

for i in range(1,51):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%5==0:
        print("Buzz")
    elif i%3==0:
        print("Fizz")
    else:
        print(i)
"""
#calculating factorial
"""
number= int(input("enter a number for factorial:"))
fact=1
for i in range(1,number+1):
    fact = fact *i

print("the factorial is", fact)
"""   
#checking prime number
"""
def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            return False
    return True

n = int(input("enter a number: "))
print("prime" if prime(n) else "not prime")
"""


#returning the squares of a list
"""
def squares(list1):
	return [ n*n for n in list1]

#making a list and passing it to the def
list1=[]
size=int(input("enter the size: "))

for i in range(size):
    element=int(input(f"enter number {i+1}: "))
    list1.append(element)

    new_list=squares(list1)
print(new_list)
"""
#removing duplicates
"""
def remove_dup(l1):
    print(list(dict.fromkeys(l1))) 


list1=[]
size=int(input("enter the size: "))

for i in range(size):
    element=int(input(f"enter number {i+1}: "))
    list1.append(element)

    #calling function
remove_dup(list1) """

#checking palindrome using lambda function
"""
palindrome = lambda s : s == s[::-1]
palindrome("anna")

"""



# ------------------------------------------------------------------
#
15
# def fibo(n):
#     if n <= 1:
#         return n
#     else:
#         return (fibo(n - 1) + fibo(n - 2))
#
#
# num= int(input("Enter your number"))
#
# # check if the number of terms is valid
# if num <= 0:
#     print("Plese enter a positive integer")
# else:
#     print("Fibonacci sequence:")
#     print(fibo(num))
#

#-----------------------------
16
from typing import List


def parse_list(inp: str) -> List[int]:
    return [int(num) for num in inp.split(",")]


user_input_1 = parse_list(input("Enter list of integers (separated by comma): "))


print(f"Average {sum(user_input_1) / len(user_input_1)}")
# # __________________________________
17
# for i in range(1, 11):
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")

#----------------------------------------------
18
#
# users = {}
#
#
# def register():
#     user = input("Enter username: ")
#     pass_ = input("Enter password: ")
#     users[user] = pass_
#
#
# def login():
#     user = input("Enter username: ")
#     pass_ = input("Enter password: ")
#     print("Login done"
#           if users.get(user) == pass_
#           else "Login not done")
#
#
# print("Register:")
# register()
#
# print("Login:")
# login()
#-----------------------------------------------------
19
user_input = input("Enter input")
words = user_input.lower().split(" ")

d = dict()
for word in words:
    if word in d:
        d[word] += 1
    else:
        d[word] = 1

print(d)

#------------------------------------------
20
def convert_temp():
    user_input = float(input("Enter int: "))
    unit = input("C or F: ").upper()
    print(user_input * 9 / 5 + 32 if unit == 'F' else (user_input - 32) * 5 / 9)


convert_temp()

#-----------------------------------------------------------------