"""
Diagonal Difference

Given a square matrix of size N x N, calculate the
absolute difference between the sums of its diagonals.
"""

#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)
sum1 = 0
sum2 = 0
for idx in range(len(a)):
    sum1 += a[idx][idx]
    sum2 += a[idx][len(a) - 1 - idx]
print abs(sum1 - sum2)
