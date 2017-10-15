"""
Beautiful Days at the Movies:

Lily likes to play games with integers and their reversals. For some integer
x, we define reversed(x) to be the reversal of all digits in x. For example,
reversed(123) = 321, reversed(21) = 12, and reversed(120) = 21.

Logan wants to go to the movies with Lily on some day x satisfying
i <= x <= j, but he knows she only goes to the movies on days she considers
to be beautiful. Lily considers a day to be beautiful if the absolute value
of the difference between x and reversed(x) is evenly divisible by k.

Given i, j, and k, count and print the number of beautiful days when Logan
and Lily can go to the movies.
"""

i, j, k = map(int, raw_input().strip().split())

count = 0
for num in xrange(i, j+1):
    rev = int(str(num)[::-1])
    if abs(num - rev)%k == 0:
        count += 1

print count

"""
Input:
20 23 6

Output:
2
"""
