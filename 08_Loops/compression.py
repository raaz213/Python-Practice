# Comprehensions (Shortcuts for Loops)
# 1. List Comprehension

squares = [x * x for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]

# 2. Dictionary Comprehension

nums = [1, 2, 3]
squares = {n: n * n for n in nums}
print(squares)  # {1: 1, 2: 4, 3: 9}

# 3. Set Comprehension

nums = [1, 2, 2, 3]
unique_squares = {x * x for x in nums}
print(unique_squares)  # {1, 4, 9}
