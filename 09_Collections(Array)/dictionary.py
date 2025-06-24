my_dict = {
    "name": "Raj",
    "age": 24,
    "country": "Nepal"
}

# print(my_dict["name"])        # Raj
# my_dict["age"] = 25           # Update value
my_dict["email"] = "raj@example.com"  # Add new key-value
# print(my_dict)
#print all key names
for data in my_dict:
    print(data) # name, age, country, email
    
# print all values
for data in my_dict:
    print(my_dict[data]) # Raj, 25, Nepal, raj@example.com
    
# Print all key and values
for key, value in my_dict.items():
    print(key, ':' , value) # name: Raj, age: 25, country: Nepal, email: raj@example.com