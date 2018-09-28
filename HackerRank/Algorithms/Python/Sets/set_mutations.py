# https://www.hackerrank.com/challenges/py-set-mutations/problem

"""
`.update() or |=`
Update the set by adding elements from an iterable/another set.

`.intersection_update() or &=`
Update the set by keeping only the elements found in it and an iterable/another
set.

`.difference_update() or -=`
Update the set by removing elements found in an iterable/another set.

`.symmetric_difference_update() or ^=`
Update the set by only keeping the elements found in either set, but not in both.
"""

A = int(raw_input().strip())
set_A = set(map(int, raw_input().strip().split()))
N = int(raw_input().strip())

for _ in range(N):
    op, n = raw_input().strip().split()
    other_set = set(map(int, raw_input().strip().split()))
    cmd = "set_A." + op + "(other_set)"
    exec(cmd)

print sum(list(set_A))
