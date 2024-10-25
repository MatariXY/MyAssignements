# Numb = int(input("enter a number: "))
#
# while Numb > 0:
#     print(Numb)
#     Numb -= 1

# total_sum = 0
#
# while True:
#     user_input = input("enter a number or 'sum'")
#
#     if user_input.lower() == "sum":
#         print("sum of positive numb: ", total_sum)
#         break
#
#     if user_input.isdigit():
#         number = int(user_input)
#         if number > 0:
#             total_sum += number
#     else:
#         print("enter only a number or 'sum'")

import random

lower_bound = int(input("lower limit: "))

upper_bound = int(input("upper limit: "))

random_number = random.randint(lower_bound, upper_bound)

lives = 5

while lives > 0:
    guess = int(input("enter your number: "))
    if guess > random_number:
        print("number is higher")
    elif guess < random_number:
        print("number is lower")
    else:
        print("you won")

    lives -= 1

    if lives == 0:
        print("you lost. right number was: ", random_number)
    else:
        print(f"remaining life:  {lives}")
