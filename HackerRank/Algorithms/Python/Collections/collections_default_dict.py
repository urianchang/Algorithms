# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

A = defaultdict(list)
B = []
n, m = map(int, raw_input().split())

for i in range(n):
    w = raw_input().strip()
    A[w].append(i+1)

for _ in range(m):
    B.append(raw_input().strip())

for word in B:
    if word in A:
        print ' '.join(map(str, A[word]))
    else:
        print -1
