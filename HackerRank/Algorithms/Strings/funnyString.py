"""
Funny String:

Suppose you have a String, S, of length N that is indexed from 0 to N - 1. You
also have some String, R, that is the reverse of String S. S is funny if the
condition abs(S[i] - S[i-1]) = abs(R[i] - R[i-1]) is true for every character
i from 1 to N-1.

Note: For some String S, S[i] denotes the ASCII value of the i-th 0-indexed
character in S. The absolute value of an integer, x, is written as abs(x).
"""

for _ in xrange(int(raw_input().strip())):
    S = raw_input().strip()
    c = len(S)
    isFunny = True
    for i in xrange(1, c):
        if abs(ord(S[i])-ord(S[i-1])) != abs(ord(S[c-1-i]) - ord(S[c-i])):
            # print S[i], S[i-1], S[c-1-i], S[c-i]
            isFunny = False
            print "Not Funny"
            break
    if isFunny:
        print "Funny"

"""
Input:
2
acxz
bcxz

Output:
Funny
Not Funny
"""
