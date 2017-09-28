"""
The Full Counting Sort

In this challenge, you need to print the data that accompanies each integer
in a list. In addition, if two strings have the same integers, you need to
print the strings in their original order. Hence, your sorting algo should
be 'stable' (i.e. the original order should be maintained for equal elements).

Given a list that contains both integers and strings, print strings in order
of their accompanying integers. If integers for two strings are equal, ensure
that they are print in the order they apeared in the original list.

TWIST: Don't print the first half of the original array. Print a dash for any
element from the first half.
"""

n = int(raw_input().strip())
count = 0
l = []
max_val = 0
while count < n:
    integer, string = raw_input().strip().split()
    integer = int(integer)
    max_val = integer if integer > max_val else max_val
    l.append([integer, string])
    count += 1

# Create list of counts
c = [0] * (max_val + 1)
for i in xrange(len(l)):
    c[l[i][0]] += 1

# Iterate through count list and add up previous values
p = 0
for i in xrange(max_val+1):
    p += c[i]
    c[i] = p

# Iterate through list backwards, compare to count list, and insert into sorted list
half = n / 2
s = [""] * n
for i in xrange(len(l)):
    rev = len(l) - 1 - i
    val = "-" if rev < half else l[rev][1]
    s[ c[l[rev][0]] - 1 ] = val
    c[l[rev][0]] -= 1

print " ".join(s)

"""
Sample input:
20
0 ab
6 cd
0 ef
6 gh
4 ij
0 ab
6 cd
0 ef
6 gh
0 ij
4 that
3 be
0 to
1 be
5 question
1 or
2 not
4 is
2 to
4 the

Sample output:
- - - - - to be or not to be - that is the question - - - -
"""
