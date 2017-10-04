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

# Function for plotting lava effect on the matrix
def plotLava(a, x, y, w, n):
    x_right = x
    x_left = x
    y_top = y
    y_bottom = y
    og = w

    while w > 0:
        w -= 1
        diff = og - w
        x_right += 1
        y_top -= 1
        x_left -= 1
        y_bottom += 1

        # row where volcano erupted
        if (x_right < n):
            a[y][x_right] += w
        if (x_left >= 0):
            a[y][x_left] += w

        # top rows
        if (y_top >= 0):
            a[y_top][x] += w
            count1 = count2 = diff
            w_right = w
            w_left = w
            for fwd in xrange(x+1, n):
                if count1 != 0:
                    a[y_top][fwd] += w
                    count1 -= 1
                else:
                    w_right -= 1
                    if w_right < 0:
                        continue
                    a[y_top][fwd] += w_right
            for bwd in reversed(xrange(0, x)):
                if count2 != 0:
                    a[y_top][bwd] += w
                    count2 -= 1
                else:
                    w_left -= 1
                    if w_left < 0:
                        continue
                    a[y_top][bwd] += w_left

        # bottom rows
        if (y_bottom < n):
            a[y_bottom][x] += w
            count_bot = count_bot2 = diff
            w_right2 = w
            w_left2 = w
            for fwd in xrange(x+1, n):
                if count_bot != 0:
                    a[y_bottom][fwd] += w
                    count_bot -= 1
                else:
                    w_right2 -= 1
                    if w_right2 < 0:
                        continue
                    a[y_bottom][fwd] += w_right2
            for bwd in reversed(xrange(0, x)):
                if count_bot2 != 0:
                    a[y_bottom][bwd] += w
                    count_bot2 -= 1
                else:
                    w_left2 -= 1
                    if w_left2 < 0:
                        continue
                    a[y_bottom][bwd] += w_left2

# Function for creating the study area matrix
def createArea(n):
    return [[0]*(n) for _ in xrange(n)]

if __name__ == "__main__":
    n = int(raw_input().strip())    # Dimension of the square study area
    m = int(raw_input().strip())    # Number of active volcanoes in area
    # If only 1 volcano, return the power of lava
    if m == 1:
        x, y, w = map(int, raw_input().strip().split())
        print w
    else:
        studyArea = createArea(n)
        for a0 in xrange(m):
            x, y, w = raw_input().strip().split(' ')
            x, y, w = [int(x), int(y), int(w)]

            # Plot volcano epicenter
            studyArea[y][x] += w
            plotLava(studyArea, x, y, w, n)

        # Find max lava effect of the study area
        max_effect = 0
        for row in studyArea:
            if max(row) > max_effect:
                max_effect = max(row)
        print max_effect

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
