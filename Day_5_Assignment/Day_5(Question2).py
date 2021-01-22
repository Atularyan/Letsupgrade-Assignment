"""
Question 2
Implement selection sort algorithm using Python.
"""

def selection_sort(arr):
    length=len(arr)
    for i in range(length-1):
        minIndex=i
        for j in range(i+1,length):
            if arr[j]<arr[minIndex]:
                minIndex=j
        arr[i],arr[minIndex]=arr[minIndex],arr[i]

arr=[int(x) for x in input("Enter the array = ").split()]
selection_sort(arr)
print("sSorted array = ",arr)