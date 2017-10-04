"""
Cavity Map:

You are given a square map of size n x n. Each cell of the map has a value
denoting its depth. We will call a cell of the map a cavity if and only if
this cell is not on the border of the map and each cell adjacent to it has
strictly smaller depth. Two cells are adjacent if they have a common side
(edge).

You need to find all the cavities on the map and depict them with the
uppercase character X.
"""

n = int(raw_input().strip())
grid = []
grid_i = 0
for grid_i in xrange(n):
    grid_t = str(raw_input().strip())
    grid.append(grid_t)

"""
Sample Input:
4
1112
1912
1892
1234

Sample Output:
1112
1X12
18X2
1234
"""
