"""
Grid Challenge:

URL: https://www.hackerrank.com/challenges/grid-challenge/problem
"""

for _ in xrange(int(raw_input().strip())):
    isImpossible = False
    G = []
    N = int(raw_input().strip())
    for _ in xrange(N):
        row = sorted(list(raw_input().strip()))
        isImpossible = (len(row) != N)
        G.append(row)

    if not isImpossible:
        for col_idx in xrange(N):
            for row_idx in xrange(1, N-1):
                if G[row_idx][col_idx] < G[row_idx-1][col_idx]:
                    isImpossible = True
                    break
            if isImpossible:
                break

    print "NO" if isImpossible else "YES"
