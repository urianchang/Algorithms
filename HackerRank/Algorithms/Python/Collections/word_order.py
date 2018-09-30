# https://www.hackerrank.com/challenges/word-order/problem
from __future__ import print_function
from collections import OrderedDict, Counter


# Method 1
od = OrderedDict()
for _ in range(int(raw_input())):
    word = raw_input()
    if word in od:
        od[word] += 1
    else:
        od[word] = 1

print(len(od.keys()))
print(*od.values())

# Method 2
# Even easier way is creating an OrderedCounter object
# https://docs.python.org/3.6/library/collections.html#ordereddict-examples-and-recipes
class OrderedCounter(Counter, OrderedDict):
    pass

oc = OrderedCounter(raw_input() for _ in range(int(raw_input())))
print(len(oc))
print(*oc.values())
