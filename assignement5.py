# N1

# mylist = [36, 73, 1, 7, 54, 100, 237, 34, 76, 10, 7, 9 , 12, 34, 49]
#
# element1 = mylist[2]
# element2 = mylist[8]
# element3 = mylist[13]
#
# result = element1 + element2 + element3
#
# print("result: ", result)


# N2

# import random
#
# mylist = [random.randint(1, 100) for _ in range(20)]
# print("original list:", mylist)
#
# odd_list = [num for num in mylist if num % 2 != 0]
# print("odd numbers:", odd_list)
#
# if odd_list:
#     smallest = odd_list[0]
#     largest = odd_list[0]
#
#     for num in odd_list:
#         if num < smallest:
#             smallest = num
#         if num > largest:
#             largest = num
#
#     print("smallest number:", smallest)
#     print("largest number:", largest)
# else:
#     print("no odd numbers were found in the list.")


# N3

# my_llist = [43, '22', 12, 66, 210, ["hi"]]
#
# index_of_210 = my_llist.index(210)
# print(f"index of 210: {index_of_210}")
#
# my_llist[-1].append("hello")
# print("Updated list after adding 'hello' to last element: ", my_llist)
#
# del my_llist[2]
# print("The updated list after deleting the item at the second index:", my_llist)
#
# my_llist_2 = my_llist.copy()
# my_llist_2.clear()
#
# print("my_llist:", my_llist)
# print("my_llist_2 (cleared):", my_llist_2)


# N4

# matrix_1 = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# matrix_2 = [
#     [9, 8, 7],
#     [6, 5, 4],
#     [3, 2, 1]
# ]
#
# result_matrix = [[0 for _ in range(len(matrix_1[0]))] for _ in range(len(matrix_1))]
#
# for i in range(len(matrix_1)):
#     for j in range(len(matrix_1[0])):
#         result_matrix[i][j] = matrix_1[i][j] + matrix_2[i][j]
#
# print("sum of two matrices:")
# for row in result_matrix:
#     print(row)

#5

# matrix = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
#
# transposed_matrix = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         transposed_matrix[j][i] = matrix[i][j]
#
# print("Transposed matrix:")
# for row in transposed_matrix:
#     print(row)


# N6

import random

matrix = [[random.randint(1, 100) for _ in range(4)] for _ in range(4)]

print("4x4 matrix of random numbers: ")
for row in matrix:
    print(row)

