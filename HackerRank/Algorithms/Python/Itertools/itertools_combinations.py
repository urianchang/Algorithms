# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

S, k = raw_input().strip().split()

for i in range(1, int(k)+1):
    for c in combinations(sorted(S), i):
        print ''.join(c)
