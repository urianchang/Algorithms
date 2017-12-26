"""
Largest Permutation

URL: https://www.hackerrank.com/challenges/largest-permutation/problem
"""

N, K = map(int, raw_input().strip().split())   # size of list and maximum swaps
perm = map(int, raw_input().strip().split())   # permutation of the first N natural numbers

s = 0
p = 0

while s < K and p < N:
    mx = perm.index(max(perm[p:]))
    if mx == p:
        p += 1
    else:
        perm[p], perm[mx] = perm[mx], perm[p]
        p += 1
        s += 1

print ' '.join(str(n) for n in perm)
