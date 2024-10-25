# 1

# squared_numbers = {x**2 for x in range(1, 11)}
# print(squared_numbers)

# 2

# user_input = input("enter string: ")
# unique_characters = set(user_input)
# print(unique_characters)

# 3

# tuple1 = (1, 2, 3, 4, 5, 6)
# tuple2 = (4, 5, 5, 6, 6, 7)
#
# combined_tuple = tuple(set(tuple1 + tuple2))
#
# duplicated_values = list(set([x for x in tuple1 if tuple2.count(x) > 0]))
#
# print("combined_tuple:", combined_tuple)
# print("duplicated_values:", duplicated_values)

# 4

# my_tuple = (1, 2, 3, 4)
#
# swapped_tuple = (my_tuple[-1],) + my_tuple[1:-1] + (my_tuple[0],)
#
# print(swapped_tuple)

# 5

# nested_tuple = (1, (2, 3), (4, (5, 6)))
#
# def flatten_tuple(t):
#     result = []
#     for item in t:
#         if isinstance(item, tuple):
#             result.extend(flatten_tuple(item))
#         else:
#             result.append(item)
#     return tuple(result)
#
# flattened_tuple = flatten_tuple(nested_tuple)
#
# print(flattened_tuple)

# 6

set1 = {1, 2}
set2 = {'a', 'b'}

result_set = {(x, y) for x in set1 for y in set2}

print(result_set)
