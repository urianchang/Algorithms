"""
Electronics Shop:

Monica wants to buy exactly one keyboard and one USB drive from her favorite
electronics store. The store sells 'n' different brands of keyboards and 'm'
different brands of USB drives. Monica has exactly 's' dollars to spend, and
she wants to spend as much of it as possible.

Given the price lists for the store's keyboards and USB drives, find and print
the amount of money Monica will spend. If she doesn't have enough money to buy
one keyboard AND one USB drive, print -1 instead.

NOTE: She will never buy more than one keyboard and one USB drive even if she
has the leftover money to do so.
"""

import sys

def getMoneySpent(keyboards, drives, s):
    combos = []
    for keyboard in keyboards:
        for drive in drives:
            if (keyboard + drive) <= s:
                combos.append(keyboard + drive)
            else:
                combos.append(-1)
    return max(combos)

s, n, m = map(int, raw_input().strip().split())
keyboards = map(int, raw_input().strip().split())
drives = map(int, raw_input().strip().split())
print getMoneySpent(keyboards, drives, s)

"""
Sample Input 0:
10 2 3
3 1
5 2 8

Sample Output 0:
9

Sample Input 1:
5 1 1
4
5

Sample Output 1:
-1
"""
