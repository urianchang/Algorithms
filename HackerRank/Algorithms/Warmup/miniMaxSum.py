"""
Mini-Max Sum

Given five positive integers, find the minimum and maximum
values that can be calculated by summing exactly four of the
five integers. Then print the respective minimum and maximum
values as a single line of two space-separated long integers.
"""

from itertools import combinations

def sumArray(arr):
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    return sum

arr = map(int, raw_input().strip().split(' '))
# arr = [1, 2, 3, 4, 5]
arr = map(sumArray, list(combinations(arr, 4)))
arr.sort()
print arr[0], arr[len(arr) - 1]
