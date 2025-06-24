#Defining and calling the  function
# def greet():
#     print('Hello')
    
# greet() # Calling the function

#Function with parameters and returns

# def sum(a,b):
#     return a+b
# print(sum(5,6)) # Calling the function with parameters

# #Default parameters

# def greet(name='Guest'):
#     print(f'Hello {name}')
# greet('Raj')
# greet() # Calling the function with default parameter

#  *args
# Example1
# def add(*args):
#     print(sum(args))
# add(2,3,4)

# #Example2

# def fruits(*args):
#     for i in args:
#         print(i)
# fruits('apple','banana','cherry')

# # **Kwargs

# def info(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key} : {value}')
# info(name='Raj',age=25,city='Bangalore')

# Lambda Function

#Example 1
# x = lambda a,b : a+b
# print(x(5,6)) # Calling the lambda function

# # Example 2
# x = lambda a,b,c : a+b+c
# print(x(5,6,7)) # Calling the lambda function

# Example 3
# x = lambda a, b, c: a if a > b and a > c else (b if b > c else c)
# print(x(2,5,7)) 

# # Example 4
# names = ["Raj", "Anil", "Binita"]
# # Sort by string length
# sorted_names = sorted(names, key=lambda name: len(name))
# print(sorted_names)

# Assignment 1 : 1.	Create a function that takes any number of numbers using *args and returns their average.

def average(*args):
    return sum(args) / len(args)
print(average(1,2,3,4,5)) # Output: 3.

#Assignment 2 : 2.	Create a lambda function that checks if a number is even or odd.
#Taking input form user
num = int(input('enter no: '))
even_odd = lambda x: "even" if x % 2 == 0 else "odd"
print(even_odd(num)) # Output: even or odd


# Assigning value directly
# x = lambda n : 'even' if n % 2 == 0 else 'odd'
# print(x(5)) # Output: odd