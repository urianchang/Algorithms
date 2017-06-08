"""
Day 5: Loops

Given an integer 'n' print its first 10 multiples.
Each multiple n x i (where 1 <= i <= 10) should be
printed on a new line in the form: n x i = result.
"""

n = int(raw_input().strip())
for i in range(1, 11):
    print str(n) + " x " + str(i) + " = " + str(n*i)
