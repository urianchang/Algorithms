"""
Luck Balance:

URL: https://www.hackerrank.com/challenges/luck-balance/problem

N: number of preliminary contests
K: maximum number of important contests that can be lost
L: amount of luck
T: importance rating (1 == important, 0 == unimportant)
"""
N, K = map(int, raw_input().strip().split())

all_res = []
imp_res = {}

for i in xrange(N):
    L, T = map(int, raw_input().strip().split())
    if T == 1:
        imp_res[i] = L
    all_res.append(L)

if K >= len(imp_res.keys()):
    print sum(all_res)
else:
