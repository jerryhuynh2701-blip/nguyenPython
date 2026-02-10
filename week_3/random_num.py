import random

num1 = random.randint(0,9)
num2 = random.randint(0,9)

machine_answer = num1 + num2

answer  = int(input(f"What is {num1} + {num2}: "))

is_correct = (answer == machine_answer)

print(type(is_correct))

# if num1 + num2 == answer:
#     print(True)
# else:
#     print(False)