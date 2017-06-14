"""
Day 10: Binary Numbers

Given a base-10 integer, 'n', convert it to binary (base-2).
Then find and print the base-10 integer denoting the maximum
number of consecutive 1's in n's binary representation.
"""

# Function to convert number into binary (for checking purposes)
def binary(num, memo):
    if num == 0:
        return memo
    remainder = num % 2
    if remainder == 0:
        memo = "0" + memo
    else:
        memo = "1" + memo
    return binary(int(num/2), memo)

# Function to count maximum number of consecutive 1's
def countOnes(num):
    remainder = 0
    count = 0
    high = 0
    while num > 0:
        remainder = num % 2
        num = int(num/2)
        if remainder == 1:
            count += 1
            if count >= high:
                high = count
        else:
            count = 0
    return high

n = int(raw_input().strip())
print countOnes(n)
