my_list = ["apple", "banana", "cherry"]
# print(my_list[0])         # apple
# my_list.append("mango")   # Add item at last
# my_list.insert (1,"mango")   # Add item at index 1
# my_list.[0] = ‘grapes’   # Replace item of index 0
# my_list.[1:2] = [‘grapes’] # Replace item of index 1
my_list[1:3] = ['grapes','pear'] #Replace item of index 1 and 2 excluding 3
# my_list.remove("banana")  # Remove specified item
# my_list.pop ()  # Remove last item
# my_list.pop (1)  # Remove specified index
# my_list.clear ()  # Empties all items in list
for list in my_list:
    print(list) # Output: apple,grapes,pear
