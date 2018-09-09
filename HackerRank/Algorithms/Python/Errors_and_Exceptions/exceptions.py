# https://www.hackerrank.com/challenges/exceptions/problem

T = int(raw_input().strip())

for _ in range(T):
    try:
        a, b = map(int, raw_input().strip().split())
        print a/b
    except (ZeroDivisionError, ValueError) as e:
        print "Error Code: {}".format(e)
