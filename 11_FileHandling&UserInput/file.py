#  Assignment 1
# 1.	Create a file named student.txt
# 2.	Write "Hello from student file" in it
# 3.	Append "This is a second line" to it
# 4.	Read and print the content

# with open('student.txt','w') as file:
#     file.write("Hello from student file")
    
# with open('student.txt', 'a') as file:
#     file.write('\nThis is  a second line')

# with open('student.txt') as file:
#     print(file.read())
    
    
# Assignment 2:
# 1.	Ask the user 3 tasks and save them in a file named todo.txt.
# Example:
# Enter task 1: ...
# Enter task 2: ...
# Enter task 3: ...
# 2.	Read the tasks from todo.txt and print them line by line.
# 3.	Let the user add more tasks (append mode) and save them without overwriting the file.

# Input tasks from the user
task1 = input('Enter task 1: ')
task2 = input('Enter task 2: ')
task3 = input('Enter task 3: ')

# Store with newlines
tasks = [task1 + '\n', task2 + '\n', task3 + '\n']

# Write tasks to file (overwrites existing content)
with open('todo.txt', 'w') as file:
    file.writelines(tasks)

# Read and print each task line by line
print("\nCurrent Tasks:")
with open('todo.txt', 'r') as file:
    for line in file:
        print("-", line.strip())

# Ask user to add more tasks
add_more = input("\nDo you want to add more tasks? (yes/no): ").lower()

if add_more == 'yes':
    num = int(input("How many additional tasks? "))
    with open('todo.txt', 'a') as file:  # 'a' = append mode
        for i in range(1, num + 1):
            new_task = input(f"Enter task {i}: ")
            file.write(new_task + '\n')

    # Show updated task list
    print("\nUpdated Task List:")
    with open('todo.txt', 'r') as file:
        for line in file:
            print("-", line.strip())

