# https://www.hackerrank.com/challenges/the-minion-game/problem

VOWELS = ('a', 'e', 'i','o', 'u')

S = raw_input().strip().lower()
kev = 0
stu = 0

for i in range(len(S)):
    if S[i] in VOWELS:
        kev += (len(S) - i)
    else:
        stu += (len(S) - i)
    print kev, stu

if kev > stu:
    print "Kevin", kev
elif stu > kev:
    print "Stuart", stu
else:
    print "Draw"

