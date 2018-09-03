# https://www.hackerrank.com/challenges/np-min-and-max/problem
"""
`min`
Returns minimum value along given axis. By default, the axis value is None.
Therefore, it finds the minimum over all the dimensions of the input array.

`max`
Returns maximum value along given axis. By default, the axis value is None.
Therefore, it finds the maximum over all the dimensions of the input array.
"""

import numpy as np

N, M = map(int, raw_input().split())
arr = np.array([raw_input().split() for _ in range(N)], int)
print np.max(np.min(arr, axis=1))