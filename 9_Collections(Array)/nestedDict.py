# Nested Dictionary
Student = {
    "11" : {
        "name" : "Rahul",
        "age"  : 20,
        "marks" : 90
        },
        
    "12" : {
        "name" : "Raj",
        "age"  : 21,
        "marks" : 85
        }
    }
# print(Student)
print(Student["11"] ["age"])

#Loop through the nested dictionary
for key, value in Student.items(): # o/p : 11 {'name': 'Rahul', 'age': 20, 'marks':90}
    print(key, value)                    # 12 {'name': 'Raj', 'age': 21, 'marks': 85}
    
for grade, info in Student.items():
    print(grade)
    for key, value in info.items():
        print(key, ':', value)
# o/p :
# 11
# name: Rahul
# age: 20
# marks: 90
# 12
# name: Raj
# age: 21
# marks: 85
