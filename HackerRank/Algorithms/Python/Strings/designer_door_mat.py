# https://www.hackerrank.com/challenges/designer-door-mat/problem

(N, M) = map(int, raw_input().strip().split())

door_mat = []

# top half
for i in range(N/2):
    tri = 3 + (i*6)
    row = ('-' * ((M-tri)/2)) + ('.|.' * (tri/3)) + ('-' * ((M-tri)/2))
    door_mat.append(row)

# center row
center = ('-' * ((M-6)/2)) + 'WELCOME' + ('-' * ((M-6)/2))
door_mat.append(center)

# bottom half
for i in range(N/2):
    row = door_mat[(N/2 - i - 1)]
    door_mat.append(row)

print '\n'.join(door_mat)

"""
Sample Input: 9 27

Sample Output:
------------.|.------------
---------.|..|..|.---------
------.|..|..|..|..|.------
---.|..|..|..|..|..|..|.---
----------WELCOME----------
---.|..|..|..|..|..|..|.---
------.|..|..|..|..|.------
---------.|..|..|.---------
------------.|.------------
"""
