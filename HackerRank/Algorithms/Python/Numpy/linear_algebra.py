# https://www.hackerrank.com/challenges/np-linear-algebra/problem
"""
`linalg.det`
The linalg.det tool computes the determinant of an array.

`linalg.eig`
The linalg.eig computes the eigenvalues and right eigenvectors of a square array.

`linalg.inv`
The linalg.inv tool computes the multiplicative inverse of a matrix.
"""

import numpy as np

np.set_printoptions(legacy='1.13')  # Need to round to two decimal places

arr = []
for _ in range(int(raw_input().strip())):
    arr.append(map(float, raw_input().strip().split()))
print np.linalg.det(arr)