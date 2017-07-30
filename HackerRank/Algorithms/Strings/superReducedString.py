"""
Super Reduced String

Steve has a string 's' consisting of 'n' lowercase
English alphabetic letters. In one operation, he
can delete any pair of adjacent letters with same
value. For example, string 'aabcc' would become either
'aab' or 'bcc' after 1 operation.

Steve wants to reduce 's' as much as possible. To do this,
he will repeat the above operation as many times as it can
be performed. Help Steve out by finding and printing s's
non-reducible form.

Note: If the final string is empty, print 'Empty String'
"""

import sys

def super_reduced_string(s):
    # Complete this function
    a = list(s)
    i = 0
    while i < len(a) - 1:
        if a[i] == a[i + 1]:
            del a[i]
            del a[i]
            i = 0
            if len(a) == 0:
                return "Empty String"
        else:
            i += 1
    return ''.join(a)

s = raw_input().strip()
result = super_reduced_string(s)
print(result)
