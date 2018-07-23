# https://www.hackerrank.com/challenges/capitalize/problem

def solve(s):
    print ' '.join(map(str.capitalize, s.split(' ')))

solve('chris alan')
