#
# user_input = input("enter text: ")
#
# cleaned_text = ""
# for character in user_input:
#     if character.isalnum():
#         cleaned_text += character.lower()
#
# is_palindrome = True
# length = len(cleaned_text)
#
# for i in range(length // 2):
#     if cleaned_text[i] != cleaned_text[length - 1 - i]:
#         is_palindrome = False
#         break
#
# if is_palindrome:
#     print("The input text is a palindrome")
# else:
#     print("The input text isn't a palindrome")


user_input = input("enter text: ")

print("ASCII: ")
for character in user_input:
    ascii_value = ord(character)
    print(ascii_value, end=" ")
