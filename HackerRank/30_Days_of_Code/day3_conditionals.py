"""
Day 3: Intro to Conditionals

Given an integer 'n', perform the following conditional
actions:
    * If n is odd, print 'Weird'
    * If n is even and in the inclusive range of 2 to 5, print 'Not Weird'
    * If n is even and in the inclusive range of 6 to 20, print 'Weird'
    * If n is even and greater than 20, print 'Not Weird'
"""

N = int(raw_input().strip());

if N%2 != 0:
    print "Weird"
else:
    if N >= 2 and N <= 5:
        print "Not Weird"
    if N >= 6 and N <= 20:
        print "Weird"
    if N > 20:
        print "Not Weird"
