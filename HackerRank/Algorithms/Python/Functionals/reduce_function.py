# https://www.hackerrank.com/challenges/reduce-function/problem

from __future__ import print_function
from fractions import Fraction


def product(fracs):
    t = reduce(lambda x, y: x*y, fracs)
    return t.numerator, t.denominator


if __name__ == '__main__':
    fracs = [
        Fraction(*map(int, raw_input().split()))
        for _ in range(input())
    ]
    print(*product(fracs))