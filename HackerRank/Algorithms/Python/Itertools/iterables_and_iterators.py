# Python 3.7
# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import permutations

N = int(input())
ls = input().strip().split()
K = int(input())

ps = list(permutations(ls, K))
c = 0
for p in ps:
    if 'a' in p:
        c += 1

print("{0:.3f}".format(c/len(ps)))
