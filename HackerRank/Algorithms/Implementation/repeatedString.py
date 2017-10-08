"""
Repeated String:

Lilah has a string 's', of lowercase English letters that she repeated
infinitely many times.

Given an integer 'n', find and print the number of letter 'a' in the first
n letters of Lilah's infinite string.
"""

s = raw_input().strip()
n = int(raw_input().strip())

# '//' is used for floor division
print s.count('a') * (n//len(s)) + s.count('a', 0, n%len(s))

"""
Input 0:
aba
10

Output 0:
7

Input 1:
a
1000000000000

Output 1:
1000000000000
"""
