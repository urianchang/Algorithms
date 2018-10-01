# https://www.hackerrank.com/challenges/any-or-all/problem

"""
any()
This expression returns True if any element of the iterable is true.
If the iterable is empty, it will return False.

all()
This expression returns True if all of the elements of the iterable are true. If the iterable is empty, it will return True.
"""

PALINDROMIC_INTS = (
    0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
    111, 121, 131, 141, 151, 161, 171, 181, 191
)

N = int(raw_input().strip())
arr = map(int, raw_input().strip().split())
print all([n >= 0 for n in arr]) and any([num in PALINDROMIC_INTS for num in arr])
