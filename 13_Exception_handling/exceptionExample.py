#Example 1 Basic try -except example

# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("Error: Division by zero is not allowed")
    
#Example 2 Multiple except blocks

# try:
#     a = int("abc")  # This will raise a ValueError
#     # b = 10 / 0      # This will raise a ZeroDivisionError
# except ValueError:
#     print("Invalid value")
# except ZeroDivisionError:
#     print("Division by zero")

#Example 3 Multiple except blocks with user input
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Cannot divide by zero!")  # This will be printed if the user enters 0
# except ValueError:
#     print("Invalid input! Please enter a number.") # This will be printed if the user enters something that can't be converted to an integer

#Example 4 Raising an exception
# age = int(input('Enter your age: '))
# if age < 0:
#     raise ValueError("Age cannot be negative")
# print('Your age is ', age , 'years')

# Example 5 Raising an exception with a custom message
# def divide(a, b):
#     if b == 0:
#         raise ValueError("Denominator cannot be zero.")
#     return a / b

# print(divide(10, 2))
# print(divide(10, 0))  # Raises error

# Example 6 Handling exceptions with a custom error message(Generic Exception)
# try:
#     result = 10 / 0
# except ValueError as e:
#     print(e)
# OR
# try:
#     x = int("hello")
# except Exception as e:
#     print("Error occurred:", e)

#Example 7 Else block
# try:
#     print("No errors here!")
# except:
#     print("Error occurred")
# else:
#     print("Try block successful")

# Example 8 Finally block
# try:
#     print("Inside try")
# finally:
#     print("Always runs, error or not")

# OR
try:
    f = open("data.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("File not found.")
finally:
    print("This block always runs.")
  
                        




