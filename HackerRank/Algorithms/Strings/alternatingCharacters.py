"""
Alternating Characters:

You are given a string containing characters A and B only, your task is to
change it into a string such that every two consecutive characters are
different. To do this, you are allowed to delete one or more characters in the
string.

Your task is to find the minimum number of required deletions.

For example, string ABAA should be changed to ABA by deleting one character A.

Constraints:
    * 1 <= t <= 10
    * 1 <= abs(s) <= 10^5
"""

for _ in xrange(int(raw_input().strip())):
    s = raw_input().strip()
    prev_ch = s[0]
    deletions = 0
    for i in xrange(1, len(s)):
        if s[i] == prev_ch:
            deletions += 1
        else:
            prev_ch = s[i]
    print deletions

"""
Input:
5
AAAA
BBBBB
ABABABAB
BABABA
AAABBB

Output:
3
4
0
0
4
"""
