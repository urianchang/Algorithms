"""
Day 25: Running Time and Complexity

A prime is a natural number greater than 1
that has no positive divisors other than 1
and it itself. Given a number, 'n', determine
and print whether it's Prime or Not prime.
"""

def primality(n):
    if n == 0 or n == 1:
        return "Not prime"
    if n == 2 or n == 3:
        return "Prime"
    if n%2 == 0:
        return "Not prime"
    else:
        i = 3
        while i*i <= n:
            if n%i == 0:
                return "Not prime"
            i += 2
        return "Prime"

T = int(raw_input().strip())

for i in range(T):
    num = int(raw_input())
    print primality(num)
