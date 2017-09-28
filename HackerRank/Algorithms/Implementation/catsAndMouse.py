"""
Cats and a Mouse:

Two cats named A and B are standing at integral points on the x-axis.
Cat A is standing at point x and cat B is standing at point y. Both
cats run at the same speed, and they want to catch a mouse named C
that's hiding at integral point z on the x-axis.

Can you determine who will catch the mouse?

If cat A catches the mouse first, print Cat A.
If cat B catches the mouse first, print Cat B.
If both cats reach the mouse at the same time, print Mouse C.
"""

chances = int(raw_input().strip())
winners = []

for _ in xrange(chances):
    x, y, z = map(int, raw_input().strip().split())
    if abs(x - z) == abs(y - z):
        winners.append("Mouse C")
    elif abs(x - z) < abs(y - z):
        winners.append("Cat A")
    else:
        winners.append("Cat B")

for winner in winners:
    print winner

"""
Sample Input:
3
1 2 3
1 3 2
2 1 3

Sample Output:
Cat B
Mouse C
Cat A
"""
