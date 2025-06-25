# Create json_assignment.py and solve the following:

# Q1. Save Book Data
# Create a dictionary for a book (title, author, year) and save it to book.json.

import json

book = {
    "title": "Muna madan",
    "author": "B.P. Koirala",
    "year": 1955  
    }
with open('book.json', 'w') as f:
    json.dump(book, f, indent=4)

# Q2. Load and Print Book
# Read back the file and print the data neatly.

with open('book.json', 'r') as f:
    data = json.load(f)
    print("Title:", data["title"])
    print("Author:", data["author"])
    print("Year:", data["year"])

# Q3. Create JSON from List
# Convert this list to JSON and save it to a file:
# students = [
#     {"name": "Sita", "grade": "A"},
#     {"name": "Ram", "grade": "B+"}
# ]
students = [
    {"name": "Sita", "grade": "A"},
    {"name": "Ram", "grade": "B+"}
]
json_data =  json.dumps(students, indent=4)
with open('students.json','w') as f:
    f.write(json_data)

# Q4. Update JSON File
# Read students.json, add a new student, and save the updated list back.
with open('students.json','r') as f:
    data = json.load(f)
    print(data)
    # Add a new student
    data.append({"name": "Laxmi", "grade": "A+"})
    with open('students.json', 'w') as f:
        json.dump(data, f, indent=4)