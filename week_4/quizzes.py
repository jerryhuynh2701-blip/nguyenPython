import random

number1= random.randint(0,9)
number2 = random.randint(0,9)

if number1 < number2:
    number1, number2 = number2, number1

machine_answer = number1 + number2

answer = int(input(f"What is {number1} + {number2}: "))

is_correct = answer == machine_answer

print(is_correct)
