"""
Let's Play a Game

A linear board of size n contains identical squares of unit size in four
different colors: Red, Blue, Green, White. There are r Red squares, g Green
squares, b Blue squares, and w White squares. Each square has a distinct
amount of coins. A player is allowed to make a move such that if he is on a
square X, he can move either to square Y or Z according to the following rules:

    * When X = Red, Y = Green, Z = White.
    * When X = Green, Y = Red, Z = Blue.
    * When X = Blue, Y = White, Z = Green.
    * When X = White, Y = Blue, Z = Red.

A player will continue to make a move till there is no possible move left.
A player cannot revisit a square. At each move player picks up all the coins
that are in the square. Consider the sequence of moves as S. The score of a
player is defined as the length of the longest increasing subsequence of the
coins collected in each move of S.

For example if the sequence of coins picked is 1, 5, 2, 3, 4, the longest
increasing sequence here is 1, 2, 3, 4 and the size is 4.

Find the maximum possible score.
"""
import sys

def playGame(s, arr):
    # Complete this function

if __name__ == "__main__":
    n = int(raw_input().strip())
    s = raw_input().strip()
    arr = map(int, raw_input().strip().split(' '))
    result = playGame(s, arr)
    print result
