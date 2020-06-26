# Python 3.7
# https://www.hackerrank.com/challenges/triangle-quest-2/problem

# You can't take more than two lines.
# The first line (a for-statement) is already written for you.
# You have to complete the code using exactly one print statement.
# Using anything related to strings will give a score of 0.
# Using more than one for-statement will give a score of 0.

# Constraints: 0 < N < 10

for i in range(1, int(input())+1):
    # Using math:
    # pow(pow(10, i)//9, 2)
    print([1, 121, 12321, 1234321, 123454321, 12345654321, 1234567654321, 123456787654321, 12345678987654321, 12345678910987654321][i - 1])
