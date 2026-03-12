# dummy = ['b','r','o','n','c','o']

# #convert it back to string
# school = "".join(dummy)

# print(school)

numbers = [1,2,3,4,5]

for num in range(len(numbers)-1,-1,-1):
    if numbers[num] % 2 == 0:
        del numbers[num]

print(numbers)

arr = [1,2]

copy = arr[:]

copy[0] = 99

print(arr)
print(copy)


