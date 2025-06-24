# Example 1 - Simple usage
name = input('enter your name :')
age = int(input('enter your age :'))
print('Name:',name,'\nAge:',age)


# Example 2 - asking user to input filename and reading it
try:
    filename = input("Enter filename to read: ")
    with open(filename, 'r') as file:
        content = file.read()
        print("📄 File Content:\n", content)
except FileNotFoundError:
        print("❌ Error: File not found.")
finally:
        print("✅ File operation complete.\n")