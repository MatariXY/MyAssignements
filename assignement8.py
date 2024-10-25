# 1

# def is_anagram(str1, str2):
#
#     return sorted(str1.lower()) == sorted(str2.lower())
#
# word1 = input("enter first word: ")
# word2 = input("enter second word: ")
#
# if is_anagram(word1, word2):
#     print(f'"{word1}" & "{word2}" are anagrams.')
# else:
#     print(f'"{word1}" & "{word2}" are not anagrams.')

# 2

# def count_character_in_string(string, character):
#
#     return string.count(character)
#
# input_string = input("Enter the string: ")
# input_character = input("Enter a symbol: ")
#
# count = count_character_in_string(input_string, input_character)
#
# print(f'symbol "{input_character}" in a string "{input_string}" is repeated {count} times.')

# 3

def fibonacci_sequence(n):

    if n <= 0:
        return []

    elif n == 1:
        return [0]

    sequence = [0, 1]

    for i in range(2, n):
        next_value = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_value)

    return sequence


n = int(input("Enter the number of Fibonacci numbers: "))
fibonacci_list = fibonacci_sequence(n)
print(f'Fibonacci {n} number: {fibonacci_list}')
