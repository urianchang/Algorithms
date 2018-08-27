# https://www.hackerrank.com/challenges/np-inner-and-outer/problem
"""
`inner`
The inner tool returns the inner product of two arrays.

    A = numpy.array([0, 1])
    B = numpy.array([3, 4])

    print numpy.inner(A, B)     #Output : 4

`outer`
The outer tool returns the outer product of two arrays.

    A = numpy.array([0, 1])
    B = numpy.array([3, 4])

    print numpy.outer(A, B)     #Output : [[0 0]
                                #          [3 4]]
"""

import numpy as np

A = map(int, raw_input().strip().split())
B = map(int, raw_input().strip().split())

print np.inner(A, B)
print np.outer(A, B)