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

import sys

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

# Function used to find longest palindrome using Dynamic Programming
def lps(arr, rules):
    n = len(arr)

    # Create a 2D table to store results: initialize with '0'
    L = [[0 for x in range(n)] for x in range(n)]

    # Strings of length 1 are palindrome of length 1
    for i in range(n):
        L[i][i] = 1

    # Create subsequences
    # l is length of substring
    for l in range(2, n+1):
        for i in range(n-l+1):
            j = i+l-1
            while arr[i] in rules:
                arr[i] = rules[arr[i]]
            while arr[j] in rules:
                arr[j] = rules[arr[j]]
            if arr[i] == arr[j] and l == 2:
                L[i][j] = 2
            elif arr[i] == arr[j]:
                L[i][j] = L[i+1][j-1] + 2
            else:
                L[i][j] = max(L[i][j-1], L[i+1][j])

    return L[0][n-1]

# for i in range(len(a)):
#     while a[i] in rules:
#         a[i] = rules[a[i]]
print lps(a, rules)
