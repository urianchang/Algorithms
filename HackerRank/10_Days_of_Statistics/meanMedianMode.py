"""
Day 0: Mean, Median, and Mode

Given an array of N integers, calculate and print the
respective mean, median, and mode on separate lines.
"""
import numpy as np
from scipy import stats

arrayCount = raw_input()
array = map(float, raw_input().split())
print np.mean(array)
print np.median(array)
print int(stats.mode(array).mode[0])
