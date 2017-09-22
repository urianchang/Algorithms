"""
Insertion Sort - Part I

Given a sorted list with an unsorted number 'e' in the rightmost cell,
print the array every time a value is shifted in the array until
the array is fully sorted. The goal of this challenge is to follow
the correct order of insertion sort.
"""

#!/bin/python
def insertionSort(ar):
    if ar[len(ar) - 1] >= ar[len(ar) - 2]:
        printArray(ar)
    else:
        start = len(ar) - 1
        e = ar[start]
        unsorted = True
        while unsorted:
            ar[start] = ar[start - 1]
            if e >= ar[start] or start == 0:
                ar[start] = e
                unsorted = False
            start -= 1
            printArray(ar)
    return ""

def printArray(arr):
    string = ""
    for val in arr:
        string += str(val) + " "
    print string

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertionSort(ar)
