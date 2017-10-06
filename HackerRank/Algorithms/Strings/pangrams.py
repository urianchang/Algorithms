"""
Pangrams:

Roy wanted to increase his typing speed for programming contests. So, his
friend advised him to type the sentence "The quick brown fox jumps over
the lazy dog" repeatedly, because it is a pangram. Pangrams are sentences
constructed by using every letter of the alphabet at least once.

After typing the sentence several times, Roy became bored with it. So he started
to look for other pangrams.

Given a sentence s, tell Roy if it is a pangram or not.
"""

s = raw_input().strip().lower()

d = {}
for ch in s:
    if ch not in d:
        d[ch] = 1

if len(d.keys()) == 27:
    print "pangram"
else:
    print "not pangram"

"""
Input 1:
We promptly judged antique ivory buckles for the next prize

Output 1:
pangram

Input 2:
We promptly judged antique ivory buckles for the prize

Output 2:
not pangram
"""
