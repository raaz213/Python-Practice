# Writing a file
# f = open('myfile.txt','w')
# f.write('Hello, world!')
# f.close() # if you are not using with statement use close()

# Using with statement
# with open('myfile.txt', 'w') as f:
#     f.write('Hello, world!')

# Append to a file
# with open("myfile.txt", "a") as file:
#     file.write("\nThis line is appended.")
#     file.write("\nThis line is appended too.")

#Write Multiple Lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

with open("demo.txt", "w") as file:
    file.writelines(lines)


# Reading a file

# f = open('myfile.txt', 'r')
# print(f.read())
# f.close()

# Using with statement
# with open('myfile.txt') as f: # default mode is 'r' so you can omit it
#     print(f.read())

#Read Line by Line
with open("demo.txt", "r") as file:
    for line in file:
        print(line.strip())

# Read single line
# with open("demo.txt", "r") as file:
#     print(file.readline())
    
#Check if File Exists (Optional)
# import os

# if os.path.exists("demo.txt"):
#     print("File exists")
# else:
#     print("File not found")
    
# Delete a File
# import os

# if os.path.exists("demo.txt"):
#     os.remove("demo.txt")
#     print("File deleted")

