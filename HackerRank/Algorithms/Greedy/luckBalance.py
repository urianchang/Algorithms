"""
Luck Balance:

URL: https://www.hackerrank.com/challenges/luck-balance/problem

N: number of preliminary contests
K: maximum number of important contests that can be lost
L: amount of luck
T: importance rating (1 == important, 0 == unimportant)
"""
N, K = map(int, raw_input().strip().split())

count = 0
imp_res = []

for i in xrange(N):
    L, T = map(int, raw_input().strip().split())
    if T == 1:
        imp_res.append(L)
    else:
        count += L

if K >= len(imp_res):
    print count + sum(imp_res)
else:
    imp_res = sorted(imp_res)
    diff = len(imp_res) - K
    win = sum(imp_res[0:diff])
    lose = sum(imp_res[diff:])
    print count - win + lose
