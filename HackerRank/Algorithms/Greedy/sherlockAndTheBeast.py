"""
Sherlock and the Beast

URL: https://www.hackerrank.com/challenges/sherlock-and-the-beast/problem
"""

for _ in xrange(int(raw_input().strip())):
    N = int(raw_input().strip())
    counter = N
    while (counter%3 != 0):
        counter -= 5
    if counter < 0:
        print -1
    else:
        print "5"*counter + "3"*(N-counter)
