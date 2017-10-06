"""
Mars Exploration:

Sami's spaceship crashed on Mars! She sends 'n' sequential SOS messages to
Earth for help. Letters in some of the SOS messages are altered by cosmic
radiation during transmission. Given the signal received by Earth as a string,
S, determine how many letters of Sami's SOS have been changed by radiation.
"""

import sys

S = raw_input().strip()

changed = 0
for i in xrange(len(S)):
    pos = i%3
    if pos == 0 and S[i] != 'S':
        changed += 1
    if pos == 1 and S[i] != 'O':
        changed += 1
    if pos == 2 and S[i] != 'S':
        changed += 1

print changed

"""
Input 0:
SOSSPSSQSSOR

Output 0:
3

Input 1:
SOSSOT

Output 1:
1
"""
