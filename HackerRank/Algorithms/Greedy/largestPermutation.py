"""
Largest Permutation

URL: https://www.hackerrank.com/challenges/largest-permutation/problem
"""

N, K = map(int, raw_input().strip().split())   # size of list and maximum swaps
perm = map(int, raw_input().strip().split())   # permutation of the first N natural numbers

s = 0
p = 0

# Attempt 1: Time out on TC 13 - 15
# while s < K and p < N:
#     mx = perm.index(max(perm[p:]))
#     if mx == p:
#         p += 1
#     else:
#         perm[p], perm[mx] = perm[mx], perm[p]
#         p += 1
#         s += 1
#
# print ' '.join(map(str, perm))

# Attempt 2: Timeout on TC 15
d = {}
for i in xrange(N):
    d[perm[i]] = i

if K < N:
    while s < K and p < N:
        mx = d[max(perm[p:])]
        if mx == p:
            p += 1
        else:
            perm[p], perm[mx] = perm[mx], perm[p]
            d[perm[p]], d[perm[mx]] = d[perm[mx]], d[perm[p]]
            p += 1
            s += 1
else:
    perm.sort(reverse=True)

print ' '.join(map(str, perm))
