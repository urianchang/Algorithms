"""
Picking Numbers

Given an array of integers, find and print the maximum number of integers
you can select from the array such that the absolute difference between
any two of the chosen integers is <= 1.
"""

n = int(raw_input().strip())    # Number of integers in list
a = map(int, raw_input().strip().split())   # List of integers

mc = 0  # Maximum number of integers
s = set(a)  # Set from integer list

# Iterate through set and compare counts of chosen integer pairs
for num in s:
    mc = max(mc, a.count(num) + a.count(num-1))

print mc


"""
Input 0:
6
4 6 5 3 3 1

Output 0:
3

Input 1:
6
1 2 2 3 1 2

Output 1:
5
"""
