# This is a neat way of quickly loading data
wire1, wire2 = open("input.txt").read().split()
wire1, wire2 = [p.split(",") for p in [wire1, wire2]]

# Keep track of movements as a series of (x, y) coordinates
DX = {"L": -1, "R": 1, "U": 0, "D": 0}
DY = {"L": 0, "R": 0, "U": 1, "D": -1}

def get_points(directions):
    # We'll also keep track of the distance traveled so far at each point
    x, y, length = (0, 0, 0)
    points = dict()
    for cmd in directions:
        direction = cmd[0]

        # For sanity checking
        assert direction in "LRUD"

        steps = int(cmd[1:])
        for _ in range(steps):
            x += DX[direction]
            y += DY[direction]
            length += 1
            if (x, y) not in points:
                points[(x, y)] = length

    return points

p1 = get_points(wire1)
p2 = get_points(wire2)

# Find intersection points
sects = set(p1.keys()) & set(p2.keys())

# Find Manhattan distance of closest intersection point from origin (0, 0)
part1 = min([abs(x) + abs(y) for (x,y) in sects])
print(part1)    # 1431

# Find fewest total steps to reach an intersection
part2 = min([p1[point] + p2[point] for point in sects])
print(part2)    # 48012
