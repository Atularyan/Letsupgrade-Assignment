"""
Question 2
Implement binary search using python language.
(Write a function which returns the index of x in given array arr if present, else returns -1)
"""

def Binary_search(arr,ele):
    start=0
    end=len(arr)-1
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]>ele:
            end=mid-1
        elif arr[mid]<ele:
            start=mid+1
        else:
            return mid
    return -1
arr=[int(x) for x in input("Enter the array = ").split()]
ele=int(input("Enter the element = "))
a=Binary_search(arr,ele)
print("Index = ",a)
#else:
 #   print("-1")