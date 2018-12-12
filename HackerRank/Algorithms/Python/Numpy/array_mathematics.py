# https://www.hackerrank.com/challenges/np-array-mathematics/problem

import numpy as np

N, M = map(int, raw_input().strip().split())

A, B = (
    np.array([
        raw_input().strip().split()
        for _ in range(N)
    ], dtype=int)
    for _ in range(2)
)

print A+B   # np.add(A, B)
print A-B   # np.subtract(A, B)
print A*B   # np.multiply(A, B)
print A/B   # np.divide(A, B)
print A%B   # np.mod(A, B)
print A**B  # np.power(A, B)
