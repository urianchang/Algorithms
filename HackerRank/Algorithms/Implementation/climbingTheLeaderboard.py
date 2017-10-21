"""
Climbing the Leaderboard

Alice is playing an arcade game and wants to climb to the top of the
leaderboard. Can you help her track her ranking as she beats each level? The
game uses Dense Ranking, so its leaderboard works like this:
    * The player with the highest score is ranked number 1 on the leaderboard.
    * Players who have equal scores receive the same ranking number, and the
        next player(s) receive the immediately following ranking number.

When Alice starts playing, there are already n people on the leaderboard. The
score of each player i is denoted by s[i]. Alice plays for m levels, and we
denote her total score after passing each level j as alice[j]. After completing
each level, Alice wants to know her current rank.

You are given an array, 'scores', of monotonically decreasing leaderboard
scores, and another arra, 'alice', of Alice's cumulative scores for each level
of the game. You must print m integers. The j-th integer should indicate the
current rank of Alice after passing the j-th level.
"""
import sys

n = int(raw_input().strip())    # number of players on board
scores = map(int,raw_input().strip().split(' '))    # leaderboard scores (desc)
m = int(raw_input().strip())    # number of levels Alice beats
alice = map(int,raw_input().strip().split(' ')) # Alice's cumulative scores

# Dedupe the scores because only interested in rank. Sort in descending order.
leaderboard = sorted(set(scores), reverse=True)
rank = len(leaderboard)

# Iterate through Alice's scores to determine her rank at that level
for alice_score in alice:
    while rank > 0 and alice_score >= leaderboard[rank-1]:
        rank -= 1
    print rank+1

"""
Input 0:
7
100 100 50 40 40 20 10
4
5 25 50 120

Output 0:
6
4
2
1
"""
