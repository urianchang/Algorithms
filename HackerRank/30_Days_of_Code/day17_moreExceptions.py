"""
Day 17: More Exceptions

Write a Calculator class with a single method:
int power(int, int). The power method takes two
integers, n and p, as parameters and returns the
integer result of n^p. If either n or p is negative,
then the method must throw an exception with the
message: n and p should be non-negative.
"""

class Calculator:
    def power(self, int1, int2):
        if int1 < 0 or int2 < 0:
            return Exception('n and p should be non-negative')
        else:
            return pow(int1, int2)

myCalculator = Calculator()
T = int(raw_input().strip())
for i in range(T):
    n,p = map(int, raw_input().strip().split())
    try:
        ans = myCalculator.power(n, p)
        print ans
    except Exception, e:
        print e
