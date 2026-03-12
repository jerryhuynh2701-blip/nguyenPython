# def max_list(l):
#     if len(l) == 0:
#         return
#     max = l[0]
#     for i in list:
#         if i > max:
#             max = i
#     return max

# list = []

# print(max_list(list))


# def find_target(arr, target):
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return True
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             left = mid - 1
#     return False


result = 1
n = 3
while n > -3:
    print(n, end=" ")
    result *= 4
    if result > 166:
        print("*")
        break
    n -= 1
else:
    print(f"| {result}")
print("done")
