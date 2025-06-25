# Example 1: Match if string starts with "Hello"

import re

text = "Hello, Python!"
result = re.match(r"Hello", text)

if result:
    print("Matched!")
    
# Extract all the digits from the string
import re

text = "My phone number is 9841234567 and my age is 24"
numbers = re.findall(r"\d+", text)
print(numbers)  # ['9841234567', '24']


# Replace all space with -
import re

text = "Hello Python Learner"
updated = re.sub(r"\s", "-", text)
print(updated)  # Hello-Python-Learner

# Validate email format
import re

email = "test@example.com"
pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")
   
# Split text    
text = "apple,banana;orange"
parts = re.split(r"[,;]", text)
print(parts)  # ['apple', 'banana', 'orange']

