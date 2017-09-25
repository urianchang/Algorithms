"""
Counting Sort I:

Given a list of integers, can you count and output the number of times
each value appears? Hint: There's no need to sort the data, you just
need to count it.
"""

n = int(raw_input().strip())
l = map(int, raw_input().strip().split())
c = [0]*100

for i in xrange(len(l)):
    c[l[i]] += 1

print " ".join(map(str,c))
