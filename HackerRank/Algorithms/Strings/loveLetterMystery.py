"""
Love Letter Mystery:

James found a love letter his friend Harry has written for his girlfriend. James
is a prankster, so he decides to meddle with the letter. He changes all the
words in the letter into palindromes.

To do this, he follows two rules:
    1. He can reduce the value of a letter.
    2. In order to form a palindrome, if he has to repeatedly reduce the value
        of a letter, he can do it until the letter becomes a. Once a letter has
        been changed to a, it can no longer be changed.

Each reduction in the value of any letter is counted as a single operation. Find
the minimum number of operations required to convert a given string into a
palindrome.
"""

for _ in xrange(int(raw_input().strip())):
    S = raw_input().strip()
    r = 0   # Number of reductions
    for i in xrange(len(S)//2):
        r += abs(ord(S[i]) - ord(S[len(S)-1-i]))
    print r

"""
Input:
4
abc
abcba
abcd
cba

Output:
2
0
4
2
"""
