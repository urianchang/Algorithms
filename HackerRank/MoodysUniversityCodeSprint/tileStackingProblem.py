"""
Tile Stacking Problem

Harvey came up with an interesting problem about stable towers. A stable tower
of height n is a tower consisting of exactly n tiles of unit height stacked
vertically in such a way, that no bigger tile is placed on a smaller tile.

Harvey gave Mike an infinite number of tiles of sizes 1,...,m. He asked him to
calculate the number of different stable towers of height n that acan be built
from these tiles, with a restriction that he can use at most k tiles of each
size in the tower.

Since the number of different stable towers can be huge, output this number
modulo 10^9 + 7.
"""
import sys

# Submitted: 4.81/50 - Wrong Answer
def tileStackingProblem(n, m, k):
    MOD = pow(10, 9)+7
    # Edge cases
    if n == (m*k):
        return 1
    if n > (m*k):
        return 0
    combos = 0
    lvl0 = m - (k - 1)
    counter = 1
    for lvl in xrange(2, n+1):
        combos += m - (k - counter)
        counter += 1
        if counter > k:
            counter = 1
    return (combos+lvl0)%MOD


if __name__ == "__main__":
    n, m, k = raw_input().strip().split(' ')
    n, m, k = [int(n), int(m), int(k)]
    result = tileStackingProblem(n, m, k)
    print result


# 112
# 113
# 123
# 122
# 133
# 223
# 233

# 112
# 113
# 114
# 122
# 123
# 124
# 133
# 134
# 144
# 223
# 224
# 234
# 244
# 334
# 344



"""
Input 0:
3 3 1

Output 0:
1

Input 1:
3 3 2

Output 1:
7
"""
