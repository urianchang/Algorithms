# Python 3.7
"""
The power level in a given fuel cell can be found through the following process:

- Find the fuel cell's rack ID, which is its X coordinate plus 10.
- Begin with a power level of the rack ID times the Y coordinate.
- Increase the power level by the value of the grid serial number (your puzzle input).
- Set the power level to itself multiplied by the rack ID.
- Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
- Subtract 5 from the power level.
"""
import math
import numpy as np


def plvl(x, y, g):
    # Calculates the power level of a fuel cell
    r = x + 10
    p = r * y
    p += g
    p = p * r
    p = math.floor(p / 100 % 10)
    p -= 5
    return p

# Function check
# assert plvl(122, 79, 57) == -5
# assert plvl(217, 196, 39) == 0
# assert plvl(101, 153, 71) == 4


def find_max(matrix):
    # Find the x, y coordinate of the maximum value of an array matrix
    max_val = np.amax(matrix)
    y_arr, x_arr = np.where(matrix == max_val)
    x = x_arr[0] + 1
    y = y_arr[0] + 1
    return (x, y)


SN = 1309    # grid serial number
grid = np.zeros((300, 300))
for y in range(1, 301):
    for x in range(1, 301):
        grid[y-1][x-1] = plvl(x, y, SN)

power_map = {}
pgrid = np.zeros((300, 300))
for y in range(1, 298):
    for x in range(1, 298):
        # For Part 1
        # pgrid[y-1][x-1] = np.sum([grid[y-1:y+2, x-1:x+2]])

        # For Part 2: BRUTE FORCING IT
        print(f"Calculating powers for ({x}, {y})...")
        m = {grid[y-1][x-1]: 1}
        for i in range(2, 300):
            y_end = y + (i - 1)
            x_end = x + (i - 1)
            val = np.sum([grid[y-1:y_end, x-1:x_end]])
            m[val] = i
        max_power = max(m.keys())
        power_map[(x, y)] = m[max_power]
        pgrid[y-1][x-1] = max_power

x, y = find_max(pgrid)
print(f"Part 1 - {x},{y}")   # 20,43
z = power_map[(x, y)]
print(f"Part 2 - {x},{y},{z}")  # 233,271,13