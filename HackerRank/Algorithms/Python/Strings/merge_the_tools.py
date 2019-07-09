# Python 3.7
# https://www.hackerrank.com/challenges/merge-the-tools/problem
from collections import OrderedDict


s = input().strip()
k = int(input().strip())

for i in range(0, len(s), k):
    u = OrderedDict.fromkeys(s[i:i+k])
    print(''.join([c for c in u.keys()]))
