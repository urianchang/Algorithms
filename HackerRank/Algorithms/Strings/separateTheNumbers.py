"""
Separate the Numbers:

A numeric string, s, is beautiful if it can be split into a sequence of two
or more positive integers, a[1]...a[n], satisfying the following conditions:
    1. a[i] - a[i-1] = 1 for any 1 < i <= n
    2. No a[i] contains a leading zero.
    3. The contents of the sequence cannot be rearranged.

You must perform 'q' queries, where each query consists of some string s. For
each query, print whether or not the string is beautiful on a new line. If it's
beautiful, print 'YES x', where x is the first number of the increasing sequence
(if there are multiple such values of x, choose the smallest); otherwise,
print 'NO' instead.

Constraints:
    * 1 <= q <= 10
    * 1 <= abs(s) <= 32
    * Each character in s is a decimal digit from 0 to 9 (inclusive)
"""

q = int(raw_input().strip())    # Number of queries to be evaluated



"""
Input:
7
1234
91011
99100
101103
010203
13
1

Output:
YES 1
YES 9
YES 99
NO
NO
NO
NO
"""
