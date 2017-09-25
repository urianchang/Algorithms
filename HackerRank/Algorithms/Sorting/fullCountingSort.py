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
