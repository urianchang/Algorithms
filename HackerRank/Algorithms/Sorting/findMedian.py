"""
Find Median:

Given a list of numbers, can you find the median?
"""

n = int(raw_input().strip())    # n is odd
ar = map(int, raw_input().strip().split())

# Sort the array and print the median value
print sorted(ar)[int(len(ar)/2)]

"""
Sample Input:
7
0 1 2 4 6 5 3

Sample Output:
3
"""
