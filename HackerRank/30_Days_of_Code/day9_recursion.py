"""
Day 9: Recursion

Write a factorial function that takes a positive integer, 'N,'
as a parameter and prints the result of N! (N factorial).
"""

def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num - 1)

N = int(raw_input().strip())

print factorial(N)
