"""
Apple and Orange:

Sam's house has an apple tree and an orange tree that yield an abundance of
fruit. In the diagram below, the red region denotes his house, where 's' is
the start point and 't' is the end point. The apple tree is to the left of
his house, and the orange tree is to the right. You can assume the trees are
located on a single point, where the apple tree is at point 'a' and the
orange tree is at point 'b'.

When a fruit falls from its tree, it lands d units of distance from its
tree of origin along the x-axis. A negative value of d means the fruit
fell d units to the tree's left, and a positive value of 'd' means it falls
d units to the tree's right.

Given the value of d for m apples and n oranges, can you determine how many
apples and oranges will fall on Sam's house (i.e. in the inclusive range [s,t])?
Print the number of apples that fall on Sam's house as your first line of
output, then print the number of oranges that fall on Sam's house as your
second line of output.

Constraints:
    * 1 <= s,t,a,b,m,n <= 10^5
    * -10^5 <= d <= 10^5
    * a < s < t < b
"""

s, t = map(int, raw_input().strip().split())    # House start and end point
a, b = map(int, raw_input().strip().split())    # Locations of apple and orange trees
m, n = map(int, raw_input().strip().split())    # Number of apples and oranges
apples = map(int, raw_input().strip().split())  # Apple distances
oranges = map(int, raw_input().strip().split()) # Orange distances

ac = 0
for apple in apples:
    if (apple+a) >= s and (apple+a) <= t:
        ac += 1
print ac

oc = 0
for orange in oranges:
    if (orange+b) >= s and (orange+b) <= t:
        oc += 1
print oc

"""
Input:
7 11
5 15
3 2
-2 2 1
5 -6

Output:
1
1
"""
