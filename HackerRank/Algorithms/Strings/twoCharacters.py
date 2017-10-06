"""
Two Characters:

String t always consists of two distinct alternating characters. For
example, if string t's two distinct characters are x and y, then t
could be xyxyx or yxyxy but not xxyy or xyyx.

You can convert some string s to string t by deleting characters from s.
When you delete a character from s, you must delete all occurrences of
it in s. For example, if s = abaacdabd and you delete the character 'a',
then the string becomes bcdbd.

Print a single integer denoting the maximum length of t for the given s;
if it is not possible to form string t, print 0 instead.
"""

# Python 3 solution
# import sys
#
# def validate(cpy):
#     for i in range(len(cpy)-1):
#         if cpy[i] == cpy[i+1]:
#             return False
#     return True
#
# for _ in range(int(input().strip())):
#     s = input().strip()
#     st = list(set(s))
#     max_len = 0
#     for x in range(len(st)):
#         for y in range(x+1, len(st)):
#             cpy = [c for c in s if c==st[x] or c==st[y]]
#             if validate(cpy):
#                 max_len = max(max_len, len(cpy))
#     print(max_len)

# Python 2 solution
def validate(c):
    for i in range(len(c) - 1):
        if c[i] == c[i+1]:
            return False
    return True

n = int(raw_input().strip())
s = list(raw_input().strip())
st = list(set(s))
max_len = 0
for x in range(len(st)):
    for y in range(x+1, len(st)):
        cpy = [c for c in s if c==st[x] or c==st[y]]
        if validate(cpy):
            max_len = max(max_len, len(cpy))
print max_len

"""
Input:
10
beabeefeab

Output:
5
"""
