# https://www.hackerrank.com/challenges/py-set-union/problem

"""
Set.union()

The .union() operator returns the union of a set and the set of elements in an
iterable. Sometimes, the | operator is used in place of .union() operator, but
it operates only on the set of elements in set. Set is immutable to the .union()
operation (or | operation).
"""

n = int(raw_input().strip())
roll_n = set(map(int, raw_input().strip().split()))
b = int(raw_input().strip())
roll_b = set(map(int, raw_input().strip().split()))

print len(roll_n.union(roll_b))
