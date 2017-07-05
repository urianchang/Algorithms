"""
An integer P is a whole square if it
is a square of some integer Q.
Write a function that returns the number
of whole squares within the interval [A...B].

Assume that B >= A.
"""

import math # use math lib for square root, ceiling, and floor

def solution(A, B):
    a = int(math.ceil(math.sqrt(abs(A))))   # find sq root of number 1
    b = int(math.floor(math.sqrt(abs(B))))  # find sq root of number 2
    # return the difference and add 1 to be inclusive
    return b - a + 1

n1 = 4
n2 = 17
print solution(n1, n2)
