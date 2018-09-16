# https://www.hackerrank.com/challenges/py-collections-deque/problem

"""
collections.deque()

A deque is a double-ended queue. It can be used to add or remove elements from
both ends.
"""

from collections import deque

d = deque()

for _ in range(int(raw_input().strip())):
    arr = raw_input().strip().split()
    m = arr[0]
    v = int(arr[1]) if len(arr) > 1 else ""
    cmd = "d.{}({})".format(m, v)
    exec(cmd)

print " ".join(map(str, d))
