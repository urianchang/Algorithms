"""
Twin Arrays:

You are given two arrays, A and B, each containing
'n' integers. You need to choose exactly one number
from A and exactly one number from B such that the
index of the two chosen numbers is not same and
the sum of the 2 chosen values is minimum.
"""

def twinArrays(ar1, ar2):
    # Complete this function
    min1a = ar1[0]
    min1b = ar1[0]
    min2a = ar2[0]
    min2b = ar2[0]
    tie = False
    for i in range(0, len(ar1)):
        if ar1[i] < min1 and ar2[i] < min2:
            tie = True
            min1 = ar1[i]
            min2 = ar2[i]
        else:
            tie = False
            if ar1[i] < min1:
                min1 = ar1[i]
            if ar2[i] < min2:
                min2 = ar2[i]
    if not tie:
        return min1 + min2
    else:



n = int(raw_input().strip()) # Size of arrays
ar1 = map(int, raw_input().strip().split(' ')) # Array A
ar2 = map(int, raw_input().strip().split(' ')) # Array B
result = twinArrays(ar1, ar2)
print(result)
