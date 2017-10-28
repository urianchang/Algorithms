"""
Angry Professor

A Discrete Mathematics professor has a class of N students. Frustrated with
their lack of discipline, he decides to cancel class if fewer than K
students are present when class starts.

Given the arrival time of each student, determine if the class is canceled.
"""

for _ in xrange(int(raw_input().strip())):
    N, K = map(int, raw_input().strip().split())
    A = sorted(map(int, raw_input().strip().split()))
    c = 0
    for n in A:
        if n <= 0:
            c += 1
            if c == K:
                break
    print "YES" if c < K else "NO"

"""
Input:
2
4 3
-1 -3 4 2
4 2
0 -1 2 1

Output:
YES
NO
"""
