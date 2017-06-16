
"""
Transform to Palindrome:

You are given a sequence 'S' comprising of 'm' Orion letters.
You are given 'k' transformations that can be applied to S.
You may apply transformations to zero or more letters in the
sequence. When a transformation is applied to a letter,
the other letters of the string remain unaffected. You can also
apply a single transformation multiple times on the same sequence.

Print the length of the longest possible palindromic subsequence
after applying zero or more transformations on the letters of the
given sequence.
"""

n,k,m = raw_input().strip().split(' ')
n,k,m = [int(n),int(k),int(m)]
rules = {}
for a0 in xrange(k):
    x,y = raw_input().strip().split(' ')
    x,y = [int(x),int(y)]
    if x > y:
        if x in rules:
            if y < rules[x]:
                rulex[x] = y
            else:
                continue
        else:
            rules[x] = y
    else:
        if y in rules:
            if x < rules[y]:
                rules[y] = x
            else:
                continue
        else:
            rules[y] = x

a = map(int, raw_input().strip().split(' '))

for i in range(len(a)):
    while a[i] in rules:
        a[i] = rules[a[i]]

maxCount = 1
for i in range(len(a)):
    count = 0
    start = i
    end = len(a) - 1
    while start < end:
        if a[start] == a[end]:
            count += 2
            start += 1
            end -= 1
        else:
            if end - start == 1:
                count += 1
            end -= 1
    if count > maxCount:
        maxCount = count

print maxCount
