"""
Sherlock and Squares

URL: https://www.hackerrank.com/challenges/sherlock-and-squares/problem
"""
import math

"""
# This method times out for a few test cases.
for _ in xrange(int(raw_input().strip())):
    A, B = map(int, raw_input().strip().split())
    count = 0
    # Iterate through range of numbers
    for i in xrange(A, B+1):
        # If perfect square, add to count
        count += 1 if math.sqrt(i)%1 == 0 else 0
    print count
"""

# Optimized solution
for _ in xrange(int(raw_input().strip())):
    A, B = map(math.sqrt, [int(i) for i in raw_input().strip().split()])
    print int(math.floor(B) - math.ceil(A) + 1)
