"""
Counting Sort II:

Given an unsorted list of integers, output the integers in order. Hint: You
can use your previous code that counted the items to print out the actual
values in order.
"""

n = int(raw_input().strip())
l = map(int, raw_input().strip().split())
c = [0]*100
s = [0]*n

# Create list of counts
for i in xrange(len(l)):
    c[l[i]] += 1

# Iterate through count list and add up previous values
b = 0
for i in xrange(100):
    b += c[i]
    c[i] = b

# Iterate through list of integers, compare to count list, and insert into sorted list
for i in xrange(len(l)):
    num = l[i]
    s[ c[num] - 1 ] = num
    c[num] -= 1

print " ".join(map(str,s))
