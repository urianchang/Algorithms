"""
Day 0: Weighted Mean

Given an array of N integers, calculate and print the
weighted mean of the elements.
"""

count = int(raw_input())
numberArr = map(float, raw_input().split())
weightArr = map(int, raw_input().split())

sum1 = 0
sum2 = 0

for idx in range(count):
    sum1 += numberArr[idx] * weightArr[idx]
    sum2 += weightArr[idx]

print round(sum1/sum2, 1)
