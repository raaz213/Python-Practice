# my_set = {"apple", "banana", "apple"}
# print(my_set)  # {'banana', 'apple'} — no duplicates

# my_set.add("mango")
# my_set.remove("banana")
# print(my_set)  # {'apple', 'mango'}


set1 = {1, 2, 3}
set2 = {3, 4, 5}

# 1. Union

# result = set1.union(set2) # OR result = set1 | set2

# print(result)  # Output: {1, 2, 3, 4, 5}

# 2. Update

# set1.update(set2)

# print(set1)  # Output: {1, 2, 3, 4, 5}

# 3. Intersection
# result = set1.intersection(set2) # OR result = set1 & set2

# print(result)  # Output: {3}

# 4. Difference
# result = set1.difference(set2) # OR result = set1 - set2

# print(result)  # Output: {1, 2}

# 5. Symmetric Difference
result = set1.symmetric_difference(set2) # OR result = set1 ^ set2

print(result)  # Output: {1, 2, 4, 5}