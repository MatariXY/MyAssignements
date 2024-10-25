#1
#
# file_name = "numbered_lines.txt"
#
# with open(file_name, "w") as file:
#     for i in range(1, 1001):
#         file.write(f"Line {i}\n")
#
# print(f"File '{file_name}' created and 1000 lines written.")
#
# with open(file_name, "r") as file:
#     lines = file.readlines()
#     filled_lines_count = len(lines)
#
# print(f"The file contains {filled_lines_count} filled lines.")

#2
#
# def number_to_text(num):
#     number_dict = {
#         2: "Two",
#         8: "Eight",
#         10: "Ten",
#         13: "Thirteen",
#         17: "Seventeen"
#     }
#     return number_dict.get(num, "")
#
# file_name = "specific_lines.txt"
#
# with open(file_name, "w") as file:
#     for i in range(1, 18):
#         if i in [2, 8, 10, 13, 17]:
#             file.write(f"Line {i}: {number_to_text(i)}\n")
#         else:
#             file.write(f"Line {i}:\n")
#
# print(f"File '{file_name}' created with specific lines filled.")

#3
#
# def read_file(file_name):
#     with open(file_name, "r", encoding="utf-8") as file:
#         return file.readlines()
#
# def write_combined_file(file1_contents, file2_contents, output_file_name):
#     with open(output_file_name, "w", encoding="utf-8") as output_file:
#         output_file.writelines(file1_contents)
#         output_file.writelines(file2_contents)
#     print(f"Files combined and written to '{output_file_name}'.")
#
# def read_and_print_file(file_name):
#     with open(file_name, "r", encoding="utf-8") as file:
#         print(file.read())
#
# file1_name = "file1.txt"
# file2_name = "file2.txt"
# output_file_name = "combined_file.txt"
#
# file1_contents = read_file(file1_name)
# file2_contents = read_file(file2_name)
#
# write_combined_file(file1_contents, file2_contents, output_file_name)
#
# read_and_print_file(output_file_name)

#4
#
# def is_palindrome(s):
#
#     cleaned_string = ''.join(e for e in s if e.isalnum()).lower()
#     return cleaned_string == cleaned_string[::-1]
#
# def print_palindrome_lines(file_name):
#     with open(file_name, "r", encoding="utf-8") as file:
#         for line_number, line in enumerate(file, start=1):
#
#             stripped_line = line.strip()
#             if is_palindrome(stripped_line):
#                 print(f"Line {line_number} is a palindrome: {stripped_line}")
#
# file_name = "sample_text.txt"
# print_palindrome_lines(file_name)

#5
#
# def split_file_by_lines(input_file_name, lines_per_file=10):
#     with open(input_file_name, "r", encoding="utf-8") as input_file:
#         lines = input_file.readlines()
#
#     total_lines = len(lines)
#     number_of_files = (total_lines + lines_per_file - 1) // lines_per_file
#
#     for file_index in range(number_of_files):
#         output_file_name = f"output_part_{file_index + 1}.txt"
#         with open(output_file_name, "w", encoding="utf-8") as output_file:
#             start_line = file_index * lines_per_file
#             end_line = start_line + lines_per_file
#             output_file.writelines(lines[start_line:end_line])
#
#         print(f"Created file: {output_file_name} with lines {start_line + 1} to {min(end_line, total_lines)}")
#
#
# input_file_name = "large_text_file.txt"
# split_file_by_lines(input_file_name)

#6

def remove_empty_lines(input_file_name, output_file_name):
    with open(input_file_name, "r", encoding="utf-8") as input_file:
        lines = input_file.readlines()

    non_empty_lines = [line for line in lines if line.strip()]

    with open(output_file_name, "w", encoding="utf-8") as output_file:
        output_file.writelines(non_empty_lines)

    print(f"Empty lines removed and written to '{output_file_name}'.")

input_file_name = "input_file.txt"
output_file_name = "output_file.txt"
remove_empty_lines(input_file_name, output_file_name)
