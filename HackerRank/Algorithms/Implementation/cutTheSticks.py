"""
Cut the Sticks

URL: https://www.hackerrank.com/challenges/cut-the-sticks/problem
"""

N = int(raw_input().strip())
a = map(int, raw_input().strip().split())

d = {}
for v in a:
    if d.get(v):
        d[v] += 1
    else:
        d[v] = 1

for k in sorted(d.keys()):
    print N
    N -= d[k]
