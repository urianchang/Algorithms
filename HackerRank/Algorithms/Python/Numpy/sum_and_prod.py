# https://www.hackerrank.com/challenges/np-sum-and-prod/problem

"""
sum
The sum tool returns the sum of array elements over a given axis.

prod
The prod tool returns the product of array elements over a given axis.
"""

import numpy

N, M = map(int, raw_input().strip().split())

arr = []
for _ in range(N):
    arr.append(map(int, raw_input().strip().split()))

print numpy.prod(numpy.sum(numpy.array(arr), axis=0))
