# Python 3.7
from collections import defaultdict
import sys
sys.setrecursionlimit(10000)

f = "input.txt"

clay = defaultdict(bool)
with open(f, 'r') as fh:
    for line in fh:
        a, brange = line.split(',')
        if a[0] == 'x':
            x = int(a.split('=')[1])
            y1, y2 = map(int, brange.split('=')[1].split('..'))

            for y in range(y1, y2 + 1):
                clay[(x, y)] = True
        else:
            y = int(a.split('=')[1])
            x1, x2 = map(int, brange.split('=')[1].split('..'))

            for x in range(x1, x2 + 1):
                clay[(x, y)] = True

ymin, ymax = min(clay, key=lambda p: p[1])[1], max(clay, key=lambda p: p[1])[1]

settled = set()
flowing = set()

def fill(pt, direction=(0, 1)):
    flowing.add(pt)

    below = (pt[0], pt[1] + 1)

    if not clay[below] and below not in flowing and 1 <= below[1] <= ymax:
        fill(below)

    if not clay[below] and below not in settled:
        return False

    left = (pt[0] - 1, pt[1])
    right = (pt[0] + 1, pt[1])

    left_filled = clay[left] or left not in flowing and fill(left, direction=(-1, 0))
    right_filled = clay[right] or right not in flowing and fill(right, direction=(1, 0))

    if direction == (0, 1) and left_filled and right_filled:
        settled.add(pt)

        while left in flowing:
            settled.add(left)
            left = (left[0] - 1, left[1])

        while right in flowing:
            settled.add(right)
            right = (right[0] + 1, right[1])

    return direction == (-1, 0) and (left_filled or clay[left]) or \
        direction == (1, 0) and (right_filled or clay[right])


fill((500, 0))
print('part 1:', len([pt for pt in flowing | settled if ymin <= pt[1] <= ymax]))
print('part 2:', len([pt for pt in settled if ymin <= pt[1] <= ymax]))

