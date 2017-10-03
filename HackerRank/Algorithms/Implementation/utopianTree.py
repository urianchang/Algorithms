"""
Utopian Tree

The Utopian Tree goes through 2 cycles of growth every year. Each spring,
it doubles in height. Each summer, its height increases by 1 meter.

Laura plants a Utopian Tree sapling with a height of 1 meter at the onset
of spring. How tall will her tree be after N growth cycles?
"""

T = int(raw_input().strip())

def utopianGrowth(cycles):
    height = 1
    for cycle in xrange(cycles):
        if cycle%2 == 0:
            height *= 2
        else:
            height += 1
    return height

for _ in xrange(T):
    N = int(raw_input().strip())
    print utopianGrowth(N)

"""
Input:
3
0
1
4

Output:
1
2
7
"""
