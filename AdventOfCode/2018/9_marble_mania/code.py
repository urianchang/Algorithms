# Python 3.7
from collections import defaultdict


SAMPLES = [
    "9 players; last marble is worth 25 points", # high score is 32
    "10 players; last marble is worth 1618 points", # high score is 8317
    "13 players; last marble is worth 7999 points", # high score is 146373
    "17 players; last marble is worth 1104 points", # high score is 2764
    "21 players; last marble is worth 6111 points", # high score is 54718
    "30 players; last marble is worth 5807 points", # high score is 37305
]
INPUT_1 = "476 players; last marble is worth 71657 points"


def run_game(setup):
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
    return scoreboard


# Test and check with examples
expected = [32, 8317, 146373, 2764, 54718, 37305]
for idx, ex in enumerate(SAMPLES):
    scores = run_game(ex)
    high_score = max(scores.values())
    # print(f"For example {idx}, high score is: {high_score}")
    assert high_score == expected[idx]

p1_scores = run_game(INPUT_1)
p1_high = max(p1_scores.values())
print(f"Part 1 - High score is: {p1_high}") # 386018
