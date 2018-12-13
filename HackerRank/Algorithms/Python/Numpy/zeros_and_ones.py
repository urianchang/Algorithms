# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem

import numpy as np

"""
zeros
The zeros tool returns a new array with a given shape and type filled with 0's.

ones
The ones zool returns a new arary with a given shape and type filled with 1's.
"""

shape = map(int, raw_input().strip().split())
print np.zeros(shape, dtype=np.int)
print np.ones(shape, dtype=np.int)
