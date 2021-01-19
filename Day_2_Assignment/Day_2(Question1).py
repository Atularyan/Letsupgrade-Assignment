"""Question 1
Write a Python program to print even numbers in a list.
Sample:
Input: list1 = [12, 3, 55, 6, 144]
Output: [12, 6, 144]
Input: list2 = [2, 10, 9, 37]
Output: [2, 10]"""

n=[int(i) for i in input("Input: List1 = ").split(",")]
k=[]
for i in n:
    if i%2==0:
        k.append(i)
print("Output : ",k)