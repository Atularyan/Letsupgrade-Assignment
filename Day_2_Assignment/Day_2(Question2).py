"""
Question 2
Write a program to print the following pattern
    1
   22
  333
 4444
55555
"""
n=int(input("Enter the number = "))
for i in range(1,n+1):
    print(" "*(n-i),str(i) * i)