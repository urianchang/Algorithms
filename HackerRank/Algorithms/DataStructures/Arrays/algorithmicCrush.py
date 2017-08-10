'''
Algorithmic Crush:

You are given a list of size 'N', initialized with zeroes. You have to perform
'M' operations on the list and output the maximum of final values of all the
'N' elements in the list. For every operation, you are given three integers,
'a', 'b', and 'k'. You have to add value k to all the elements ranging from index
a to b (both inclusive).
'''

"""
Sample input:
5 3
1 2 100
2 5 100
3 4 100

Output:
200
"""

N, M = map(int, raw_input().strip().split(' '))

l = [0] * (N+1)

for _ in range(M):
    a, b, k = map(int, raw_input().strip().split(' '))
    # Only store the difference
    l[a-1] += k
    if b <= len(l):
        l[b] -= k

maximum = x = 0
# Iterate through the list, adding up the values to find the max 
for i in l:
    x = x + i
    maximum = max(x, maximum)

print maximum

'''
This solution times out after Test Case #6...

maximum = 0

for _ in xrange(M):
    a, b, k = map(int, raw_input().strip().split(' '))
    for num in range(a, b+1):
        l[num] += k
        if l[num] > maximum:
            maximum = l[num]

print maximum
'''
