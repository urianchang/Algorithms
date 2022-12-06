# https://leetcode.com/problems/unique-paths/
from math import factorial as fact


def uniquePaths(m: int, n: int) -> int:
    # Subtract 1 from each position to account for origin and end positions
    right = m - 1
    down = n - 1

    # Total moves that the robot has to take
    moves = right + down

    # Find combination of moves: moves!/(right! * down!)
    return int(fact(moves)/(fact(right) * fact(down)))


assert uniquePaths(3, 7) == 28
