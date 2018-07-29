# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations
# This tool returns successive _r_ length permutations of elements in an iterable.
# If _r_ is not specified or is None, then _r_ defaults to the length of the iterable.

S, k = raw_input().strip().split()

word_list = sorted([''.join(word) for word in list(permutations(S, int(k)))])

print '\n'.join(word_list)
