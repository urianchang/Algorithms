"""
Day 1: Quartiles

Given an array, X, of n integers, calculate
the respective first quartile, second quartile,
and third quartile.
"""

e = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
# e = 12
# s = "4 17 7 14 18 12 3 16 10 4 4 12"
# arr = map(int, s.strip().split(' '))
arr.sort()

def showMid(a):
    if len(a)%2 != 0:
        return a[len(a)/2]
    return (a[len(a)/2] + a[len(a)/2 - 1])/2

if e%2 != 0:
    L = arr[:(e/2)]
    U = arr[(e/2 + 1):]
else:
    L = arr[:(e/2)]
    U = arr[(e/2):]

print showMid(L)
print showMid(arr)
print showMid(U)
