# for i in range(1, 10):
#     if i == 5:
#         continue
#     print(i) # 1 2 3 4 6 7 8 9 (skip 5)


for i in range(10):
    if i % 2 == 0:
        continue
    print(i) # 1 3 5 7 9 (skip even numbers)