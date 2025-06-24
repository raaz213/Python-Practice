#  Q1. Safe Division
# Ask two numbers and divide them. Handle:
# •	Division by zero
# •	Non-numeric input

# try:
#     a = int(input('Enter a 1st number: '))
#     b = int(input('Enter a 2nd number: '))
#     result = a / b
# except ZeroDivisionError:
#     print('Division by Zero')
# except ValueError:
#     print('Non-numeric input')
# else:
#     print(result)

# Q2. File Reader with Try-Except
# Ask the user for a filename and try to read it.
# •	Show proper message if file does not exist.

# try:
#         filename = input("Enter filename to read: ")
#         with open(filename, 'r') as file:
#             content = file.read()
#             print("File Content:\n", content)
# except FileNotFoundError:
#         print("Error: File not found.")
# 
    
    
# Q3. Raise Custom Exception
# Write a function check_age(age) that raises an error if age is less than 0.

# age = int(input('Enter your age: '))
# def check_age(age):
#     if age < 0:
#         raise ValueError('Age cannot be negative')
#     print('Your age is :',age)
# check_age(age)

# Q4. Use Finally Block
# Use try-except-finally to print:
# "All done." (even if error occurs)

try:
    x = 10 / 0
except ZeroDivisionError:
    print('Cannot be divided by Zero')
finally:
    print("All done.")



    
