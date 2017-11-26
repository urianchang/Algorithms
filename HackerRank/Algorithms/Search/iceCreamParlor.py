"""
Ice Cream Parlor:

HackerRank url: https://www.hackerrank.com/challenges/icecream-parlor/problem
"""

def ice_cream_combo(m, n, c):
    d = {}
    for i in xrange(0, (n-1)):
        for j in xrange(i+1, n):
            price = c[i] + c[j]
            if price == m:
                return "{} {}".format(i+1, j+1)
            if price < m:
                d[price] = "{} {}".format(i+1, j+1)
    return d[d.keys().sort()[-1]]

for _ in xrange(int(raw_input().strip())):
    m = int(raw_input().strip())    # money
    n = int(raw_input().strip())    # ice cream flavors
    c = map(int, raw_input().strip().split())   # flavor price
    print ice_cream_combo(m, n, c)
