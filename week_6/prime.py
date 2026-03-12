# def is_prime(num):
#     if num == 2 or num == 3:
#         return True

#     if num % 2 == 0:
#         return False

#     for i in range(3, num, 2):
#         if num % i == 0:
#             return False
#         else:
#             return True


# is_prime(7)

# def f(x):
#     def g():
#         x = "abc"
#         print(f"from g, x = {x}")
#     def h():
#         z = x
#         print(f"from h, z = {z}")
#     x = x + 1
#     print(f"from x, x = {x}")
#     h()
#     g()
#     print(f"from x, x = {x}")
#     return g

# x = 3

# z = f(x)

# print(f"x = {x}")
# print(f"z = {z}")

# z()



