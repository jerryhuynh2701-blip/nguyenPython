numbers = [10,25,30,45,60,75,90]

new_arr = filter(lambda x: x > 30 and x % 5 == 0, numbers)

print(list(new_arr))