# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

# N <= 15
fib = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377]

N = int(raw_input())
print map(lambda x: x**3, fib[:N])
