# Python 3.7
# https://www.hackerrank.com/challenges/minimum-distances/problem
from typing import List


def minimumDistances(a: List[int]) -> int:
    m = {}
    for idx, n in enumerate(a):
        if n in m:
            m[n].append(idx)
        else:
            m[n] = [idx]

    d = []
    for group in m.values():
        if len(group) == 2:
            d.append(abs(group[0] - group[1]))

    return -1 if not d else min(d)


assert minimumDistances([7, 1, 3, 4, 1, 7]) == 3

n = int(input())
a = list(map(int, input().rstrip().split()))
result = minimumDistances(a)
print(result)
