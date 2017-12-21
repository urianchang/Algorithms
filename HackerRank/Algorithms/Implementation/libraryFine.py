"""
Library Fine

URL: https://www.hackerrank.com/challenges/library-fine/problem
"""
d1, m1, y1 = map(int, raw_input().strip().split())
d2, m2, y2 = map(int, raw_input().strip().split())

sum=0
if(y1>y2):
    sum+=10000
elif(y1>=y2 and m1>m2):
    sum+=500*(m1-m2)
elif(y1>=y2 and m1>=m2 and d1>d2):
    sum+=15*(d1-d2)
print(sum)
