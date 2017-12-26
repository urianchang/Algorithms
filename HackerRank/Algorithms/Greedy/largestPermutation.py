"""
Largest Permutation

URL: https://www.hackerrank.com/challenges/largest-permutation/problem
"""

N, K = map(int, raw_input().strip().split())   # size of list and maximum swaps
perm = map(int, raw_input().strip().split())   # permutation of the first N natural numbers

p = 0

# Attempt 1: Time out on TC 13 - 15
# s = 0
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
# Attempt 3: Fix how index dictionary was used
d = {}
for i in xrange(N):
    d[perm[i]] = i

if K < N:
    while K > 0 and p < N:
        if perm[p] == N - p:
            p += 1
        else:
            max_idx = d[N - p]
            d[N-p], d[perm[p]] = d[perm[p]], d[N-p]
            perm[max_idx], perm[p] = perm[p], perm[max_idx]
            p += 1
            K -= 1
else:
    perm.sort(reverse=True)

print ' '.join(map(str, perm))
