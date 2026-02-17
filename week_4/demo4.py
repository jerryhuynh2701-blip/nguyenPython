import random

num = random.randint(0,10)

is_correct = False

num_guess = 0

while not is_correct and num_guess < 3 :
    user_num = int(input("Guess the number: "))
    if user_num < num:
        print("Too low")
    elif user_num > num:
        print("Too high")
    else:
        print('Correct')
        is_correct = True
    num_guess += 1
print("game over")