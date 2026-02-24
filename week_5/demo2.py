# def my_func():
#     x = 200
#     x = x + 10
#     print(x)

# x = 5
# my_func()
# print(x)

# def arr_func():
#     arr.append(500)
#     print(arr)

# arr = [1,2,3]
# arr_func()

# print(arr)

# def is_divisible_by_three(num):
#     if num % 3 == 0:
#         print("True")
#     else:
#         print("False")

def is_in(string_1, string_2):
    if not string_1 or not string_2:
        return False
    return (string_1 in string_2) or (string_2 in string_1)

print(is_in('cat','concatanation'))


