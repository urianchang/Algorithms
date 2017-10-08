"""
Weighted Uniform Strings:

A weighted string is a string of lowercase English letters where each letter
has a weight in the inclusive range from 1 to 26.

The weight of a string is the sumb of the weights of all the string's
characters.

A uniform string is a string consisting of a single character repeated zero
or more times.

Given a string, s, let U be the set of weights for all possible uniform
substrings (contiguous) of string s. You have to answer n queries, where
each query i consists of a single integer x[i]. For each query, print
YES on a new line if x[i] is a member of U; otherwise, print NO.
"""

import sys

s = raw_input().strip()
n = int(raw_input().strip())

ALPHA = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26
}

# Create dictionary of substring values
d = {}
# weight0 = ALPHA[s[0]]
# d[weight0] = 1
#
# for i in xrange(len(s)):
#     if i == len(s)-1:
#         d[ALPHA[s[i]]] = 1
#         break
#     else:
#         weight = ALPHA[s[i]]
#         d[weight] = 1
i = 0
while i < len(s):
    code = ALPHA[s[i]]
    d[code] = 1
    idx = i + 1
    while idx < len(s) and s[idx] == s[i]:
        code += ALPHA[s[i]]
        d[code] = 1
        idx += 1
    i = idx

for a0 in xrange(n):
    x = int(raw_input().strip())
    # your code goes here
    if x in d:
        print "Yes"
    else:
        print "No"

"""
Input:
abccddde
6
1
3
12
5
9
10

Output:
Yes
Yes
Yes
Yes
No
No
"""
