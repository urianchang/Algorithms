# https://www.hackerrank.com/challenges/np-concatenate/problem
"""
Two or more arrays can be concatenated together using the concatenate
function with a tuple of the arrays to be joined.

If an array has more than one dimension, it is possible to specify the
axis along which multiple arrays are concatenated. By default, it is
along the first dimension.
"""

import numpy as np

N, M, P = map(int, raw_input().strip().split())

arr1 = np.array([raw_input().split() for _ in range(N)], int)
arr2 = np.array([raw_input().split() for _ in range(M)], int)
print np.concatenate((arr1, arr2), axis=0)
