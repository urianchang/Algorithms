# https://www.hackerrank.com/challenges/np-eye-and-identity/problem
"""
identity
The identity tool returns an identity array. An identity array is a square
matrix with all the main diagonal elements as 1 and the rest as 0. The default
type is float.

eye
The eye tool returns a 2-D array with 1's as the diagonal and 0's elsewhere. The
diagonal can be main, upper or lower, depending on the optional parameter, `k`.
A positive `k` is the upper diagonal, a negative `k` is for the lower, and a 0
`k` (defualt) is for the main diagonal.
"""
import numpy as np


np.set_printoptions(sign=' ') # Add space in front of each element

N, M = map(int, raw_input().strip().split())
print(np.eye(N, M))
