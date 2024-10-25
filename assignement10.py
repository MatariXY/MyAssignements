# 1

# def zip_lists(list1, list2):
#     return [str(item) for item in zip(list1, list2)]
#
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
#
# result = zip_lists(list1, list2)
# print(result)

# 2

# get_even_numbers = lambda lst: list(filter(lambda x: x % 2 == 0, lst))
#
# lst = [1, 2, 3, 4, 5, 6, 7]
#
# result = get_even_numbers(lst)
# print(result)

# 3

# get_positive_numbers = lambda lst: list(filter(lambda x: x > 0, lst))
#
# lst = [-10, -5, 0, 5, 10]
#
# result = get_positive_numbers(lst)
# print(result)

# 4

# is_palindrome = lambda lst: list(filter(lambda s: s == s[::-1], lst))
#
# lst = ['madam', 'hello', 'racecar', 'python', 'level']
#
# result = is_palindrome(lst)
# print(result)

# 5

# from functools import reduce
#
# def multiply_elements(lst):
#     try:
#         return reduce(lambda x, y: x * y, lst)
#     except TypeError:
#         return "TypeError: Please provide a list of numbers."
#
# lst = [1, 2, 3, 4, 5]
#
# result = multiply_elements(lst)
# print(result)

# 6

# def filter_by_ending(strings_list, ending):
#     try:
#         return list(filter(lambda s: s.endswith(ending), strings_list))
#     except TypeError:
#         return "TypeError: Please provide a valid list of strings and a valid ending string."
#
# strings_list = ['hello', 'world', 'coding', 'nod']
# ending = 'ing'
#
# result = filter_by_ending(strings_list, ending)
# print(result)