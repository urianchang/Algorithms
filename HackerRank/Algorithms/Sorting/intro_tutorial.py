"""
Intro to Tutorial Challenges

Given a sorted array and a number, can you print the index location of
the number in the array?
"""

def locate(val, arr):
    for i in xrange(len(arr)):
        if arr[i] == val:
            return i

v = int(raw_input().strip())
c = int(raw_input().strip())
a = map(int, raw_input().strip().split())
print locate(v, a)

"""
Sample Input:
4
6
1 4 5 7 9 12

Sample Output:
1
"""
