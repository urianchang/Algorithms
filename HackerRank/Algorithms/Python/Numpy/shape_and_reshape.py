# https://www.hackerrank.com/challenges/np-shape-reshape/problem

"""
shape
The shape tool gives a tuple of array dimensions and can be used to change the
dimensions of an array

reshape
The reshape tool gives a new shape to an array without changing its data. It
creates a new array and does not modify the original array itself
"""

import numpy as np

print np.reshape(np.array(raw_input().strip().split(), int), (3, 3))
