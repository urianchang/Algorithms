# Python 3.7
import time
import sys
from collections import namedtuple

FILE = 'input.txt'

Point = namedtuple('Point', ['x', 'y', 'dx', 'dy'])
points = []
with open(FILE, 'r') as fh:
    for line in fh:
        a = line.strip().split('=')
        pos = a[1].lstrip('<').split('>')[0].split(',')
        vel = a[2].lstrip('<').rstrip('>').split(',')
        points.append(Point(
            x = int(pos[0].strip()),
            y = int(pos[1].strip()),
            dx = int(vel[0].strip()),
            dy = int(vel[1].strip())
        ))

# Find iteration where points are closest together
ivals = {}
for i in range(20000):
    minx = min(p.x + i * p.dx for p in points)
    maxx = max(p.x + i * p.dx for p in points)
    miny = min(p.y + i * p.dy for p in points)
    maxy = max(p.y + i * p.dy for p in points)

    val = maxx - minx + maxy - miny
    ivals[val] = i

closest_i = ivals[min(ivals.keys())] # 10630

# Plot out the closest alignment
map = [
    [' '] * 200 for _ in range(400)
]
for p in points:
    x = p.x + closest_i * p.dx
    y = p.y + closest_i * p.dy
    map[y][x] = "*"

for m in map:
    print(''.join(m))

# Message: LRCXFXRP


"""Animated plot that only really works for the sample

def move_points(ps):
    new = []
    for p in ps:
        nx = p.x + p.dx
        ny = p.y + p.dy
        new.append(Point(x=nx, y=ny, dx=p.dx, dy=p.dy))
    return new


def make_map(ps, xmax, ymax):
    p_dict = {(p.x, p.y): "#" for p in ps}
    for y in range(0, ymax+1):
        for x in range(0, xmax+1):
            if (x, y) in p_dict:
                sys.stdout.write('#')
            else:
                sys.stdout.write('.')
        print()


xs = [p.x for p in points]
min_x = min(xs)
max_x = max(xs)
ys = [p.y for p in points]
min_y = min(ys)
max_y = max(ys)

norm = []
for p in points:
    if min_x < 0:
        x = p.x + abs(min_x)
    else:
        x = p.x - abs(min_x)
    if min_y < 0:
        y = p.y + abs(min_y)
    else:
        y = p.y - abs(min_y)
    norm.append(Point(x=x, y=y, dx=p.dx, dy=p.dy))

count = 0
print(count)
make_map(norm, max_x, max_y)

count += 1
stars = move_points(norm)

while True:
    print(count)
    make_map(stars, max_x, max_y)
    count += 1
    stars = move_points(stars)
    time.sleep(1)
"""