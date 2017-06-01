"""
Plus Minus

Given an array of integers, calculate which fraction of its
elements are positive, which fraction of its elements are
negative, and which fraction of its elements are zeroes,
respectively. Print the decimal value of each fraction on a new line.
"""

#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
pos = 0.0
neg = 0.0
zero = 0.0
total = 0.0
for num in arr:
    # print num
    if num == 0:
        zero += 1
    if num > 0:
        pos += 1
    if num < 0:
        neg += 1
    total += 1
print pos/total
print neg/total
print zero/total
