# https://www.reddit.com/r/adventofcode/comments/a6wpup/2018_day_17_solutions/ebzesnu/
from collections import defaultdict
import re
import sys
sys.setrecursionlimit(10000)

clay = defaultdict(bool)
settled, flowing = set(), set()
inp = open('input.txt').read()

for line in inp.split("\n"):
    a, b, c = map(int, re.findall("([\d]+)", line))
    if line.startswith('x='):
        for y in range(b, c+1):
            clay[a + y * 1j] = True
    else:
        for x in range(b, c+1):
            clay[x + a * 1j] = True

yl = [p.imag for p in clay]
ymin, ymax = min(yl), max(yl)
print("ymin", "ymax", ymin, ymax, "clay fields",len(clay))

def fill(p, direction= 1j ):
    flowing.add(p)
    below, left, right = p+1j, p-1, p+1

    if not clay[below]:
        if below not in flowing and 1 <= below.imag <= ymax:
            fill(below)
        if below not in settled:
            return False

    l_filled = clay[left]  or left  not in flowing and fill(left , direction=-1)
    r_filled = clay[right] or right not in flowing and fill(right, direction=1)
    #print("left_right_filled", left_filled, right_filled)

    if direction == 1j and l_filled and r_filled:
        settled.add(p)

        while left in flowing:
            settled.add(left)
            left -= 1

        while right in flowing:
            settled.add(right)
            right += 1

    return direction == -1 and (l_filled or clay[left]) or \
           direction ==  1 and (r_filled or clay[right])

fill(500)

print('part 1:', len([pt for pt in flowing | settled if ymin <= pt.imag <= ymax]))
print('part 2:', len([pt for pt in settled if ymin <= pt.imag <= ymax]))