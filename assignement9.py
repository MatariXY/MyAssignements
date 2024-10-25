# 1

# int_list = [10, 20, 30, 40]
# def add_to_int_list(number):
#     global int_list
#     int_list.append(number)
#
# user_input = int(input("enter number: "))
#
# add_to_int_list(user_input)
#
# print(f"Updated list: {int_list}")

# 2

# def sum_of_digits(number):
#
#     if number == 0:
#         return 0
#     else:
#
#         return number % 10 + sum_of_digits(number // 10)
#
# user_input = int(input("enter number: "))
#
# result = sum_of_digits(user_input)
# print(f"The sum of the digits of a number {user_input} is: {result}")

# 3
# def reverse_string(s):
#     if s == "":
#         return s
#     else:
#         return s[-1] + reverse_string(s[:-1])
# user_input = input("Enter the string: ")
# result = reverse_string(user_input)
# print(f"The inverted string is: {result}")

# 4
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
n = int(input("Enter the size of the Fibonacci sequence: "))
fibonacci_sequence = [fibonacci(i) for i in range(n)]
print(f"Fibonacci sequence ({n} element): {fibonacci_sequence}")
