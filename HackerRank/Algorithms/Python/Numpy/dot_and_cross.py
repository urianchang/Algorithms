# https://www.hackerrank.com/challenges/np-dot-and-cross/problem
"""
`dot`
The dot tool returns the dot product of two arrays.

    A = numpy.array([ 1, 2 ])
    B = numpy.array([ 3, 4 ])

    print numpy.dot(A, B)       #Output : 11

`cross`
The cross tool returns the cross product of two arrays.

    A = numpy.array([ 1, 2 ])
    B = numpy.array([ 3, 4 ])

    print numpy.cross(A, B)     #Output : -2
"""

import numpy as np

A = []
B = []

N = int(raw_input().strip())

for _ in range(N):
    a = map(int, raw_input().strip().split())
    A.append(a)

for _ in range(N):
    b = map(int, raw_input().strip().split())
    B.append(b)

# "Matrix product" == `dot product`
print np.dot(A, B)