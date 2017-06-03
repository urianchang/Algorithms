"""
Day 1: Interquartile Range

Given an array 'X' of 'n' integers and an array 'F'
representing the respective frequencies of X's elements,
construct a data set 'S' where each 'x' occurs at frequency
'f'. Then calculate and print S's interquartile range,
rounded to a scale of 1 decimal place.
"""

e = int(raw_input().strip())
x = map(int, raw_input().strip().split(' '))
f = map(int, raw_input().strip().split(' '))

def showMid(a):
    if len(a)%2 != 0:
        return round(float(a[len(a)/2]), 1)
    return round(float((a[len(a)/2] + a[len(a)/2 - 1])/2.0), 1)

s = []
for i in range(e):
    for idx in range(f[i]):
        s.append(x[i])
s.sort()
e = len(s)
if e%2 != 0:
    L = s[:(e/2)]
    U = s[(e/2 + 1):]
else:
    L = s[:(e/2)]
    U = s[(e/2):]
print showMid(U) - showMid(L)
