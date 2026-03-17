# nums = [10, 25, 30, 45, 60, 75, 90]

# new_nums = filter(lambda x: x % 10 == 0 , nums)

# list = [n ** 2 for n in new_nums]

# print(list)


# find the largest number using reduce()
from functools import reduce

numbers = [15, 3, 27, 9, 42, 8]

num_large = reduce(lambda x, y: x if x > y else y, numbers)

print(num_large)

# calculate total number of chars using reduce()
print(f"******************")

words = ["Python", "is", "powerful", "and", "simple"]

total = reduce(lambda y, x: y + len(x), words, 0)

print(total)
