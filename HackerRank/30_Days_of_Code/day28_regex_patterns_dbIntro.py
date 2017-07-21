"""
Day 28: RegEx, Patterns, and Intro to Databases

Consider a database table, 'Emails', which has the
attributes, 'First Name' and 'Email ID'. Given rows
of data simulating the 'Emails' table, print an
alphabetically-ordered list of people whose email
address ends in @gmail.com.
"""

import sys

N = int(raw_input().strip())

for a0 in xrange(N):
    firstName, emailID = raw_input().strip().split(' ')
    firstName, emailID = [str(firstName),str(emailID)]
    print firstName
    print emailID
