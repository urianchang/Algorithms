"""
Day 1: Standard Deviation

Given an array 'X' of 'N' integers, calculate and
print the standard deviation. Your answer should be
in decimal form, rounded to a scale of 1 decimal place.
An error margin of +/- 0.1 will be tolerated for the standard deviation.
"""
import math

# c = 5
# e = [10, 40, 30, 50, 20]
c = int(raw_input().strip())
e = map(int, raw_input().strip().split(' '))
e.sort()

m = 0
for i in range(c):
    m += e[i]
m = m/float(c)

v = 0
for i in range(c):
    v += (e[i] - m) ** 2
print round(math.sqrt(v/c), 1)
