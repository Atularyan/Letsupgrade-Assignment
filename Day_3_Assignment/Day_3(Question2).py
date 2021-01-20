"""
Question 2
Define a function swap that should swap two values and print the swapped variables outside the
swap function.
"""

def swap(n):
    rev=0
    while(n>0):
        rem=n%10
        rev=(rev*10)+rem
        n=n//10
    return (rev+n)
n=int(input("Enter the number = "))
res=swap(n)
print("swapped value = ",res)