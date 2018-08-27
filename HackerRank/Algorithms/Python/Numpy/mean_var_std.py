# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem
"""
`mean`
The mean tool computes the arithmetic mean along the specified axis.
By default, the axis is `None`. Therefore, it computes the mean of
the flattened array.

`var`
The var tool computes the arithmetic variance along the specified axis.
By default, the axis is None. Therefore, it computes the variance of
the flattened array.

`std`
The std tool computes the arithmetic standard deviation along the
specified axis.
By default, the axis is None. Therefore, it computes the standard
deviation of the flattened array.
"""

import numpy as np

N, M = map(int, raw_input().strip().split())
arr = []

for _ in range(N):
    arr.append(map(int, raw_input().strip().split()))

# To pass the test, list has to be printed with a space after the first `[`
np.set_printoptions(legacy='1.13')
print np.mean(arr, axis=1)
print np.var(arr, axis=0)
print np.std(arr)