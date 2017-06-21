"""
Day 20: Bubble Sort

Given an array, 'a', of size 'n' distinct elements,
sort the array in ascending order using the Bubble
Sort algorithm above. Once sorted, print the following
3 lines:
    1. Array is sorted in numSwaps swaps.
    2. First Element: firstElement
    3. Last Element: lastElement
"""

import sys

n = int(raw_input().strip())
a = map(int, raw_input().strip().split(' '))
# Write Your Code Here
numSwaps = 0
for i in range(n):
    numberOfSwaps = 0
    for idx in range(n-1):
        if a[idx] > a[idx+1]:
            a[idx], a[idx+1] = a[idx+1], a[idx]
            numberOfSwaps += 1
    if numberOfSwaps == 0:
        break
    else:
        numSwaps += numberOfSwaps
print "Array is sorted in", numSwaps, "swaps"
print "First Element:", a[0]
print "Last Element:", a[n-1]
