###################################
#1
###################################
# def positive_number_check(func):
#     def wrapper(number):
#         if number < 0:
#             raise ValueError("რიცხვი უნდა იყოს დადებითი")
#         result = func(number)
#         print(f"შედეგი: {result}")
#         return result
#     return wrapper
#
# @positive_number_check
# def return_number(number):
#     return number
#
# try:
#     return_number(5)
#     return_number(-3)
# except ValueError as e:
#     print(e)
###############################
#2
###############################
# class PositiveNumberChecker:
#     def __call__(self, number):
#         if number < 0:
#             raise ValueError("რიცხვი უნდა იყოს დადებითი")
#         print(f"შედეგი: {number}")
#         return number
#
# number_checker = PositiveNumberChecker()
#
# try:
#     number_checker(5)
#     number_checker(-3)
# except ValueError as e:
#     print(e)
################################
#3
################################
# import time
#
# def execution_time_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"ფუნქციის შესრულების დრო: {execution_time:.6f} წამი")
#         return result
#     return wrapper
#
# @execution_time_decorator
# def sample_function():
#     time.sleep(2)
#     print("ფუნქცია შესრულდა")
#
# sample_function()
##########################################
#4
##########################################
class LoggingMeta(type):
    def __new__(cls, name, bases, attrs):
        print(f"კლასის შექმნა: {name}")

        methods = [attr for attr, value in attrs.items() if callable(value)]
        print(f"{name} კლასის მეთოდები: {methods}")

        return super().__new__(cls, name, bases, attrs)

class ExampleClass(metaclass=LoggingMeta):
    def method_one(self):
        pass

    def method_two(self):
        pass

example = ExampleClass()
