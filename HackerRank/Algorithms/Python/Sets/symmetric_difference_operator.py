# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

"""
'.symmetric_difference()'

The .symmetric_difference() operator returns a set with all the elements that
are in the set and the iterable but not both.

Sometimes, a ^ operator is used in place of the .symmetric_difference() tool,
but it only operates on the set of elements in set.

The set is immutable to the .symmetric_difference() operation (or ^ operation).
"""

n = int(raw_input().strip())
roll_n = set(map(int, raw_input().strip().split()))
b = int(raw_input().strip())
roll_b = set(map(int, raw_input().strip().split()))

# print len(roll_n.symmetric_difference(roll_b))
print len(roll_n ^ roll_b)
