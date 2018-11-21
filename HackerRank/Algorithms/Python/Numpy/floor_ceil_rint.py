# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem

"""
floor
The tool floor returns the floor of the input element-wise.

ceil
The tool ceil returns the ceiling of the input element-wise.

rint
The rint tool rounds to the nearest integer of input element-wise.
"""

import numpy

numpy.set_printoptions(sign=' ') # For the answer to be accepted, we need whitespace
arr = numpy.array(map(float, raw_input().strip().split()))

print numpy.floor(arr)
print numpy.ceil(arr)
print numpy.rint(arr)
