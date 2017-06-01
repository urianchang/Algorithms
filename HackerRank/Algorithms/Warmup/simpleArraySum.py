"""
Simple Array Sum

Given an array of N integers, can you find the sum of its elements?
"""

#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
sum = 0
for num in arr:
    sum += num
print sum
