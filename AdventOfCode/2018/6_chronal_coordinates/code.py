# Python 3.7
from collections import defaultdict
import numpy as np


def manhattan(p1: list, p2: list) -> int:
    """The distance between two points is the sum of the absolute differences of
    their Cartesian coordinates.

    Reference: https://en.wikipedia.org/wiki/Taxicab_geometry
    """
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def calculate_counts(max_x, min_x, max_y, min_y, bounds) -> (dict, int):
    """For each point in a grid, calculate its Manhattan distance from each
    coordinate. Keep count of the coordinate closest to each point. If more than
    one coordinate is closest, skip the count. The count for each coordinate
    represents the area that it occupies.
    """
    safe_area = 0
    counts = defaultdict(lambda: 0)
    for row in range(min_y-bounds, max_y+bounds):
        for col in range(min_x-bounds, max_x+bounds):
            distances = {}
            for i, c in enumerate(coordinates):
                distances[i] = manhattan([col, row], c)

            # Part 2: Safe area is where distance to all coordinates < 10000
            if sum(distances.values()) < 10_000:
                safe_area += 1

            closest_distance = min(distances.values())
            closest_coord = [
                k for k, v in distances.items()
                if v == closest_distance
            ]
            # print(f"distances: {distances}, closest_val: {closest_val}, closest_coord: {closest_coord}")
            if len(closest_coord) == 1:
                counts[closest_coord[0]] += 1
    return (counts, safe_area)


coordinates = []
with open('input.txt', 'r') as fh:
    for line in fh:
        x, y = line.strip().split(',')
        coordinates.append(
            (int(x.strip()), int(y.strip()))
        )

n = np.array(coordinates, dtype=int)
maxX, maxY = n.max(0) # [8 9] [353 357]
minX, minY = n.min(0) # [1 1]

# Find areas twice with different grid boundaries
c1, s1 = calculate_counts(maxX, minX, maxY, minY, 10)
c2, s2 = calculate_counts(maxX, minX, maxY, minY, 20)

# The ones not effected by the changed boundaries are not 'infinite'
finite_counts = []
for k, v in c1.items():
    if c2[k] == v:
        finite_counts.append(v)

print(f"Part 1 - The largest finite area is: {max(finite_counts)}") # 4887

# The safe region should be equal regardless of the grid boundaries
assert s1 == s2
print(f"Part 2 - Area of the safe zone: {s1}")
