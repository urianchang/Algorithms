"""
The Hurdle Race:

Dan is playing a video game in which his character competes
in a hurdle race by jumping over n hurdles with heights h0, h1,
h2,... He can initially jump a maximum height of k units, but
he has an unlimited supply of magic beverages that help him
jump higher! Each time Dan drinks a magic beverage, the maximum
height he can jump during the race increases by 1 unit.

Given n, k, and the heights of all the hurdles, find and print
the minimum number of magic beverages Dan must drink to complete
the race.
"""

n, k = map(int, raw_input().strip().split())
maxHeight = max(map(int, raw_input().strip().split()))

drinks = maxHeight - k

print drinks if drinks > 0 else 0

"""
Sample Input:
5 4
1 6 3 5 2

Sample Output:
2
"""
