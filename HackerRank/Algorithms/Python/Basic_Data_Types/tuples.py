"""
Tuples

Given an integer, n, and n space-separated integers as input,
create a tuple, t, of those n integers. Then compute and
print the result of hash(t).

URL: https://www.hackerrank.com/challenges/python-tuples/problem
"""

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print hash(tuple(integer_list))
