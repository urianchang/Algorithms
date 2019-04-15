# https://www.hackerrank.com/challenges/compress-the-string/problem
from itertools import groupby

S = raw_input().strip()
groups = []

for k, g in groupby(S):
    groups.append((len(list(g)), int(k)))

for g in groups:
    print g,