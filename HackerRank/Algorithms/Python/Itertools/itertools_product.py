# https://www.hackerrank.com/challenges/itertools-product/problem

from itertools import product
# This tool computes the cartesian product of input iterables.
# It is equivalent to nested for-loops.
# For example, product(A, B) returns the same as ((x,y) for x in A for y in B).

A = map(int, raw_input().strip().split())
B = map(int, raw_input().strip().split())

print(' '.join(map(str, list(product(A, B)))))
