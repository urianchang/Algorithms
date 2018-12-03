# Python 3.7
import re
import numpy as np


def get_data():
    # () -> list
    claims = []
    with open('input.txt', 'r') as fh:
        for line in fh:
            # TODO: Use regex to get numbers faster
            # Slower way of parsing the string
            parts = line.strip().split(' ')
            claim = int(parts[0].lstrip('#'))
            loc = list(map(int, parts[2].rstrip(':').split(',')))
            dim = list(map(int, parts[3].split('x')))
            claims.append((claim, loc[0], loc[1], dim[0], dim[1]))
    return claims


# Create maximum cloth and add all claim inputs
fabric = np.zeros((1000, 1000))
for (claim, x, y, l, w) in get_data():
    fabric[x:x+l, y:y+w] += 1

# Part 1: How many square inches of fabric are within two or more claims?
print(np.sum(fabric > 1))   # 121163

# Part 2: What is the ID of the only claim that doesn't overlap?
for (claim, x, y, l, w) in get_data():
    if np.all(fabric[x:x+l, y:y+w] == 1):
        print(f"unique claim: {claim}")   # 943
