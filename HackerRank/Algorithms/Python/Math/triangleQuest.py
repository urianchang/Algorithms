# Python 3.7
# https://www.hackerrank.com/challenges/python-quest-1/problem

# Use no more than two lines.
# The first line (the for statement) is already written for you.
# You have to complete the print statement.
# Note: Using anything related to strings will give a score of 0.

# Constraints: 0 <= N <= 9

for i in range(1, int(input())):
    # Using math:
    # print(pow(10, i)//9 * i)
    print([1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999][i-1])