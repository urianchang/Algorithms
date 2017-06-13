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
    if ar1[0] > ar1[1]:
        min1a = ar1[1]
        min1b = ar1[0]
    else:
        min1a = ar1[0]
        min1b = ar1[1]
    if ar2[0] > ar2[1]:
        min2a = ar2[1]
        min2b = ar2[0]
    else:
        min2a = ar2[0]
        min2b = ar2[1]
    tie = False
    for i in range(0, len(ar1)):
        if ar1[i] < min1a and ar2[i] < min2a:
            tie = True
            min1b = min1a
            min1a = ar1[i]
            min2b = min2a
            min2a = ar2[i]
        else:
            tie = False
            if ar1[i] < min1b:
                if ar1[i] < min1a:
                    min1b = min1a
                    min1a = ar1[i]
                else:
                    min1b = ar1[i]
            if ar2[i] < min2b:
                if ar2[i] < min2a:
                    min2b = min2a
                    min2a = ar2[i]
                else:
                    min2b = ar2[i]
    if tie == False:
        return min1a + min2a
    else:
        if min2b >= min1b:
            return min2a + min1b
        else:
            return min1a + min2b


n = int(raw_input().strip()) # Size of arrays
ar1 = map(int, raw_input().strip().split(' ')) # Array A
ar2 = map(int, raw_input().strip().split(' ')) # Array B
result = twinArrays(ar1, ar2)
print(result)
