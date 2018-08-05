# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict as od

orders = od()
for _ in range(int(raw_input().strip())):
    order = raw_input().strip().split()
    p = int(order.pop())
    n = ' '.join(order)

    if n in orders:
        orders[n] += p
    else:
        orders[n] = p

for item, price in orders.items():
    print "%s %s" % (item, price)