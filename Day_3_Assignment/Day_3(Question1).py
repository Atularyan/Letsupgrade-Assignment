"""
Question 1
Write a Python program to add two numbers using class and object.
(Take both numbers as input from the user)
"""
class Add:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print("Result = ",self.num1+self.num2)

num1=int(input("Enter the num1 = "))
num2=int(input("Enter the num2 = "))
Addition=Add(num1,num2)
Addition.add()