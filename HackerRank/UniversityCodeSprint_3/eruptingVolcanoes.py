"""
Erupting Volcanoes

According to recent research, most active volcanoes are located near
the islands of the Pacific Ocean. Scientists knkow the effects of the
volcanic lava and they want to measure the maximum effect of
lava on a specific area.

According to their studies, the lava has a maximum effect in the place
of the volcanic eruption, and this effect seems to decrease the further
it gets from the eruption place. More specifically, for a volcano located
in a cell (x, y) with power w, first it affects the cell (x, y) with power
w, then it affects yet-unaffected cells adjacent to recently affected cells
with power equal to the last power decreased by 1, and continues this
process until the power becomes 0.

Given the size of the study area and the coordinates of the erupting
volcanoes, find the maximum total effect value of the lava across all cells
in the experiment's area.
"""
import sys

if __name__ == "__main__":
    n = int(raw_input().strip())    # Dimension of the square study area
    m = int(raw_input().strip())    # Number of active volcanoes in area
    for a0 in xrange(m):
        x, y, w = raw_input().strip().split(' ')    # x, y = coordinates; w = power of lava
        x, y, w = [int(x), int(y), int(w)]

def plotVolcano(l, x, y, w):


"""
Sample Input:
10
1
4 5 6

Sample Output:
6

Sample Input:
10
2
3 3 3
7 7 4

Sample Output:
4
"""
