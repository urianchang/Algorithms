"""
A Very Big Sum

You are given an array of integers of size N. Print the
sum of the elements in the array.
"""

#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
sum = 0
for num in arr:
    sum += num
print sum
