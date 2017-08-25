"""
Minimum Absolute Difference in an Array:

Consider an array of integers. We define absolute difference
between two elements to be the absolute value of a1 - a2.

Given an array of 'n' integers, find and print the minimum
absolute different between any two elements in the array.
"""


import sys

def minimumAbsoluteDifference(n, arr):
    return min(abs(num1 - num2) for (num1, num2) in zip(arr, arr[1:]))

if __name__ == "__main__":
    n = int(raw_input().strip())
    arr = sorted(map(int, raw_input().strip().split(' ')))
    result = minimumAbsoluteDifference(n, arr)
    print result

'''
Sample Input:
3
3 -7 0

Sample Output:
3
'''
