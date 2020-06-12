# Python 3.7
# https://www.hackerrank.com/challenges/beautiful-triplets/problem
from typing import List


def beautifulTriplets(d: int, arr: List[int]) -> int:
    c = 0
    for el in arr:
        if el + d in arr and el + (2*d) in arr:
            c += 1
    return c


assert beautifulTriplets(3, [1, 2, 4, 5, 7, 8, 10]) == 3
assert beautifulTriplets(3, [1, 6, 7, 7, 8, 10, 12, 13, 14, 19])
