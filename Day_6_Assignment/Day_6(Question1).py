"""
Question 1
A Barua number is a number that consists of only zeroes and ones and has only one 1. Barua’s
number will start with 1. Given numbers, find out the multiplication of the numbers. Note: The
input may contain one decimal number and all other Barua numbers. (Assume that each number
is the very large and the total number of values give is also very large)
Input 1: 100 10 12 1000
Output 1: 12000000
Input 2: 100 121 1000000000000000
Output 2: 12100000000000000000
Input 3: 10 100 1000
Output 3: 1000000
"""

def barua_mul(li):
    totalzeroscount=0

    for num in li:
        check=str(num)
        flag=False
        for ch in check:
            if ch == '0' or ch=='1':
                continue
            else:
                n=check
                flag=True
                break
        if flag==True:
            continue
        else:
            totalzeroscount+=check.count('0')
    a=int(n)
    b='1'
    for i in range(totalzeroscount):
        b+='0'
    res=a*int(b)
    return res

t=int(input("Enter the no. of test cases : "))
for tc in range(t):
    li=[int(i) for i in input("Input : ").split()]
    mul_ans=barua_mul(li)
    print("Output : ",mul_ans)