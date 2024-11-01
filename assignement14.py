#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# class BankAccount:
#     def __init__(self, account_number, account_holder, balance=0.0):
#         self.account_number = account_number
#         self.account_holder = account_holder
#         self.balance = balance
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"{amount} ₾ ჩარიცხულია. ახალი ბალანსი: {self.balance} ₾")
#         else:
#             print("ჩარიცხული თანხა უნდა იყოს დადებითი.")
#
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("არასაკმარისი თანხა.")
#         elif amount <= 0:
#             print("გატანის თანხა უნდა იყოს დადებითი.")
#         else:
#             self.balance -= amount
#             print(f"{amount} ₾ გამოტანილია. ახალი ბალანსი: {self.balance} ₾")
#
#     def display(self):
#         print(f"ანგარიშის ნომერი: {self.account_number}")
#         print(f"ანგარიშის მფლობელი: {self.account_holder}")
#         print(f"ბალანსი: {self.balance} ₾")
#
# account1 = BankAccount("GE29NB0000000101904917", "ანასტასია გელაშვილი", 1000)
# account2 = BankAccount("GE29NB0000000101904918", "ლაშა კაპანაძე", 500)
#
# account1.display()
# account1.deposit(200)
# account1.withdraw(150)
# account1.display()
#
# account2.display()
# account2.deposit(100)
# account2.withdraw(700)  # არასაკმარისი თანხა
# account2.display()

########################################

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = []

    def enroll_course(self, course_name):
        if course_name not in self.courses:
            self.courses.append(course_name)
            print(f"{self.name} ჩარიცხულია {course_name} კურსზე.")
        else:
            print(f"{self.name} უკვე ჩარიცხულია {course_name} კურსზე.")

    def display_info(self):
        print(f"სტუდენტის სახელი: {self.name}")
        print(f"სტუდენტის ID: {self.student_id}")

    def display_courses(self):
        if self.courses:
            print(f"{self.name} ჩარიცხულია შემდეგ კურსებზე: {', '.join(self.courses)}")
        else:
            print(f"{self.name} არ არის ჩარიცხული არცერთ კურსზე.")

student1 = Student("ანა მახარაძე", "S001")
student2 = Student("გიორგი ყავრელიშვილი", "S002")

# კურსებზე რეგისტრაცია
student1.enroll_course("მათემატიკის")
student1.enroll_course("ქიმიის")
student2.enroll_course("ფიზიკის")
student2.enroll_course("პროგრამირების")
student2.enroll_course("ბირთვული ინჟინერიის")

student1.display_info()
student1.display_courses()

student2.display_info()
student2.display_courses()

