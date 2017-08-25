"""
Marc's Cakewalk:

Marc loves cupcakes, but he also likes to stay fit. He eats
'n' cupcakes in one sitting, and each cupcake 'i' has a calorie
count, ci. After eating a cupcake with 'c' calories, he must walk
at least 2^j * c (where j is the number of cupcakes he has already
eaten) miles to maintain his weight.

Given the individual calorie counts for each of the 'n' cupcakes,
find and print a long integer denoting the minimum number of miles
Marc must walk to maintain his weight. Note that he can eat the cupcakes
in any order.
"""

import sys

n = int(raw_input().strip())
calories = map(int, raw_input().strip().split(' '))


'''
Sample Input:
3
1 3 2

Sample Output:
11
'''
