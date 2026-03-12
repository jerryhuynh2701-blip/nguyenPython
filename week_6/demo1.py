# Change an existing string

user_name = "bronco"

new_user_name = "B" + user_name[1:]

# [start, end, step] -> end: exclusive

print(new_user_name)

# modify an item in a list

numbers = [1,2,3]
numbers[0] = 0
print(numbers)

#modify middle items

letters = ['a','b','c''d','e','f']
letters[2:5] = []
print(letters)

#Inserting elements using empty slice

numbers = [3,4,5]
numbers[0:0] = [1,2]
print(numbers)

nums = [1,2,3,4,5,6]
del nums[2:5]
print(nums)


items = ['x','y','z']
del items[:]
print(items) #[]

values = [1,2,3]
del values
print(values) #Error
