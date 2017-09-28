"""
Breaking the Records:

Maria plays n games of college basketball in a season. Because she wants to
go pro, she tracks her points scored per game sequentially in an array
defined as 'score'. After each game i, she checks to see if the new score
breaks her record for most or least points scored so far during the season.

Given Maria's array of scores for a season of n games, find and print the
number of times she breaks most and least points scored during the season.

Note: Assume her records for most and least points at the start of the
season are the number of points scored during the first game of the season.
"""

n = int(raw_input().strip())
s = map(int, raw_input().strip().split())

maxScore = s[0]
minScore = s[0]
maxCount = 0
minCount = 0

for i in xrange(len(s)):
    if s[i] > maxScore:
        maxScore = s[i]
        maxCount += 1
    elif s[i] < minScore:
        minScore = s[i]
        minCount += 1

print maxCount, minCount

"""
Sample input:
9
10 5 20 20 4 5 2 25 1

Sample output:
2 4
"""
