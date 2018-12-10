# Python 3.7
from collections import deque, defaultdict


SAMPLES = [
    "9 players; last marble is worth 25 points", # high score is 32
    "10 players; last marble is worth 1618 points", # high score is 8317
    "13 players; last marble is worth 7999 points", # high score is 146373
    "17 players; last marble is worth 1104 points", # high score is 2764
    "21 players; last marble is worth 6111 points", # high score is 54718
    "30 players; last marble is worth 5807 points", # high score is 37305
]
INPUT_1 = "476 players; last marble is worth 71657 points"
INPUT_2 = "476 players; last marble is worth 7165700 points"


def run_game(setup):
    # list insertion and deletion -> O(n^2) time
    parts = setup.strip().split()
    players = int(parts[0])
    last = int(parts[-2])

    scoreboard = defaultdict(lambda: 0)
    ring = [0]
    cursor = 0
    marble = 0
    while marble != last:
        for player in range(1, players+1):
            marble += 1

            if (marble % 23) == 0:
                scoreboard[player] += marble
                new_cursor = cursor - 7
                if new_cursor < 0:
                    new_cursor = len(ring) + new_cursor
                scoreboard[player] += ring[new_cursor]
                del ring[new_cursor]
                cursor = new_cursor
                if cursor == len(ring)+1:
                    cursor -= len(ring)
                elif cursor > len(ring):
                    cursor -= (len(ring)+1)
            else:
                cursor += 2
                if cursor == len(ring)+1:
                    cursor -= len(ring)
                elif cursor > len(ring):
                    cursor -= (len(ring)+1)
                ring.insert(cursor, marble)

            if marble == last:
                break
    return max(scoreboard.values())


def run_game_optimized(setup):
    # Use a deque ["double-ended queue" (doubly-linked list in C)]
    parts = setup.strip().split()
    max_players = int(parts[0])
    last = int(parts[-2])

    scores = defaultdict(int)
    circle = deque([0])

    for marble in range(1, last+1):
        if marble % 23 == 0:
            circle.rotate(7)
            scores[marble % max_players] += marble + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

    return max(scores.values())

# Test and check with examples
# expected = [32, 8317, 146373, 2764, 54718, 37305]
# for idx, ex in enumerate(SAMPLES):
#     hi_score = run_game(ex)
#     assert hi_score == expected[idx]
#
#     hi_2 = run_game_optimized(ex)
#     assert hi_2 == expected[idx]

p1_high = run_game(INPUT_1)
print(f"Part 1 - High score is: {p1_high}") # 386018

p2_high = run_game_optimized(INPUT_2)
print(f"Part 2 - High score is: {p2_high}") # 3085518618
