# 1

# from collections import Counter
#
# sentence = input("enter text: ").lower()
#
# words = sentence.split()
#
# word_count = Counter(words)
#
# print(dict(word_count))


# 2

# def calculator(num1, num2, operator):
#     operations = {
#         '+': num1 + num2,
#         '-': num1 - num2,
#         '*': num1 * num2,
#         '/': num1 / num2 if num2 != 0 else "Cannot be divided by zero"
#     }
#
#     return operations.get(operator, "Invalid operator")
#
#
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# operator = input("Enter a mathematical operator (+, -, *, /): ")
#
# result = calculator(num1, num2, operator)
# print(f"result: {result}")


# 3

# squares_dict = {num: num**2 for num in range(1, 11)}
#
# print(squares_dict)


# 4

departments = {
    "Sales": [
        {"first name": "Irakli", "last name": "Gogritchiani", "age": 30, "salary": 2000},
        {"first name": "Nino", "last name": "Kvaratskhelia", "age": 28, "salary": 2100}
    ],
    "Marketing": [
        {"first name": "Mariami", "last name": "Abashidze", "age": 25, "salary": 2200},
        {"first name": "Giorgi", "last name": "Cicishvili", "age": 32, "salary": 2300}
    ],
    "HR": [
        {"first name": "Sopo", "last name": "Gelashvili", "age": 27, "salary": 1800},
        {"first name": "Mikheil", "last name": "Beridze", "age": 35, "salary": 1900}
    ]
}

for department, employees in departments.items():
    total_salary = sum(employee["salary"] for employee in employees)
    average_salary = total_salary / len(employees)
    print(f"{department} Average salary of the department: {average_salary:.2f}")
