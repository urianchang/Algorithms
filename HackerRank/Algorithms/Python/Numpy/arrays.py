# https://www.hackerrank.com/challenges/np-arrays/problem

import numpy

def arrays(arr):
    numpy.set_printoptions(sign=' ') # For the answer to be accepted, we need whitespace
    return numpy.flipud(numpy.array(arr, float))

arr = raw_input().strip().split(' ')
result = arrays(arr)
print(result)

