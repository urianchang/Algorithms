"""
Day 29: Bitwise AND
Given set S = {1, 2, 3, ..., N}. Find two integers,
A and B (where A < B), from set S such that the value
of A&B is the maximum possible and also less than a
given integer, K. In this case, & represents the
bitwise AND operator.
"""

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
