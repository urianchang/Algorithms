"""
Game of Thrones - I

The king has a string composed of lowercase English letters. Help him
figure out whether any anagram of the string can be a palindrome or not.
"""

d = {}

for ch in raw_input().strip():
    if ch not in d:
        d[ch] = 1
    else:
        d[ch] += 1

isAnagram = True
count_odd = 0
for count in d.values():
    if count%2 != 0:
        count_odd += 1
    if count_odd >= 2:
        isAnagram = False
        break

print "YES" if isAnagram else "NO"

"""
Input:
cdcdcdcdeeeef

Output:
YES
"""
