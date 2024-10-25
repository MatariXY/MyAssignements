# number = int(input("Enter a number: "))
#
# if number % 2 == 0:
#     print("even")
# else:
#     print("odd")


# txt = input("enter a text: ")
#
# if "small" in txt:
#     print("small")
# elif "tall" in txt:
#     print("tall")
# elif "middle" in txt:
#     print("middle")
# else:
#     print("no words")

number1 = float(input("Enter a number: "))
number2 = float(input("Enter a number: "))


operator = input("enter an operator (+, -, /, *, //, %, **): ")

if operator == '+':
    print(number1 + number2)
elif operator == '-':
    print(number1 - number2)
elif operator == '/':
    print(number1 / number2)
elif operator == '*':
    print(number1 * number2)
elif operator == '//':
    print(number1 // number2)
elif operator == '%':
    print(number1 % number2)
elif operator == '**':
    print(number1 ** number2)