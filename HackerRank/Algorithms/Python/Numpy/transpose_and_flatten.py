# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem
"""
`transpose`
Create a new array from transposed arrays

`flatten`
Creates a copy of the input array flattened to one dimension
"""

import numpy as np

N, M = map(int, raw_input().strip().split())

arr = np.array([raw_input().split() for _ in range(N)], int)

print np.transpose(arr)
print arr.flatten()