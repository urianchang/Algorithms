"""
Between Two Sets:

Consider two sets of positive integers, A and B. We say that a positive integer,
x, is between A and B if the following conditions are satisfied:
    1. All elements in A are factors of x.
    2. x is a factor of all elements in B.

In other words, some x is between A and B if that value of x satisfies
x%a[i] == 0 for every a in A and also satisfies b[i]%x == 0 for every b in B.

Given A and B, find and print the number of integers that are between the two
sets.
"""

n, m = map(int, raw_input().strip().split())
A = map(int, raw_input().strip().split())
B = map(int, raw_input().strip().split())

# x should be gte max(A) and lte min(B)
total = 0
for x in xrange(max(A), min(B)+1):
    isBetween = False
    for a in A:
        if x % a == 0:
            isBetween = True
        else:
            isBetween = False
            break
    if isBetween:
        for b in B:
            if b % x == 0:
                isBetween = True
            else:
                isBetween = False
                break
    total += 1 if isBetween else 0

print total

"""
Input:
2 3
2 4
16 32 96

Output:
3
"""
