"""
Castle Towers

Eragon is a dragon that is visiting the town of Osaka. There are n Towers
of various heights in the city, and tower i has height of height[i].
Because the taller towers tower over the shorter ones, Eragon can only
blow out the tallest towers.

For example, assume there are four towers of heights 3, 5, 4, and 5. Then
Eragon can blow out 2 towers as there are two towers of maximum height 5.

Given the height height[i] for each individual tower, find and print the
number of towers that Eragon can successfully blow out.
"""

import sys

# n = int(raw_input().strip())
# ar = map(int, raw_input().strip().split())

n = 4
ar = [3, 2, 1, 3]

def castleTowers(n, ar):
    # Original code:
    # ar.sort(reverse = True)
    # maxi = int(ar[0])
    # count = 1
    # for x in xrange(1, len(ar)):
    #     if maxi == ar[x]:
    #         count += 1
    # return count

    # Submission 1: 98 / 100 - Timed out on last test case
    d = {}
    d[ar[0]] = 1
    maxi = ar[0]
    for i in xrange(1, n):
        if ar[i] >= maxi:
            if ar[i] > maxi:
                maxi = ar[i]
        if ar[i] in d:
            d[ar[i]] += 1
        else:
            d[ar[i]] = 1
    return d[maxi]

    # Submission 2: 49 / 100 - Timed out on last test case
    # ar.sort(reverse = True)
    # maxi = int(ar[0])
    # count = 1
    # for x in xrange(1, len(ar)):
    #     if maxi == ar[x]:
    #         count += 1
    #     else:
    #         break
    # return count

    # Final Submission: 100 / 100
    d = {}
    d[ar[0]] = 1
    maxi = ar[0]
    for i in xrange(1, n):
        if ar[i] >= maxi:
            if ar[i] > maxi:
                maxi = ar[i]
            if ar[i] in d:
                d[ar[i]] += 1
            else:
                d[ar[i]] = 1
    return d[maxi]

print castleTowers(n, ar)

"""
Input:
4
3 2 1 3

Output:
2
"""
