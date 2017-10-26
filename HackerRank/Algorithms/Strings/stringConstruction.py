"""
String Construction:

Amanda has a string, s, of m lowercase letters that she wants to copy into a
new string, p. She can perform the following operations any number of times
to construct string p:
    * Append a character to the end of string p at a cost of 1 dollar.
    * Choose any substring of p and append it to the end of p at no charge.
"""

for _ in xrange(int(raw_input().strip())):
    print len(set(list(raw_input().strip())))

"""
Input:
2
abcd
abab

Output:
4
2
"""
