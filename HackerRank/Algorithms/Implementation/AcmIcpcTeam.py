# https://www.hackerrank.com/challenges/acm-icpc-team/problem
from typing import List, Tuple

from pprint import pprint


def acmTeam(topic: List[str]) -> Tuple[int, int]:
    """

    :param topic: A list of strings, each representing a person and their knowledge on a subject
    :return: A tuple with two elements:
        1. the maximum number of topics a 2-person team can know;
        2. the number of ways to form a 2-person team that knows the maximum number of topics
    """
    max_topics = 0
    max_teams = 0
    for i in range(len(topic) - 1):
        for j in range(i+1, len(topic)):
            # Find number of topics that the team knows
            t_count = 0
            p1 = topic[i]
            p2 = topic[j]
            for t_idx in range(len(p1)):
                if p1[t_idx] == "1" or p2[t_idx] == "1":
                    t_count += 1

            if t_count > max_topics:
                max_topics = t_count
                max_teams = 1
            elif t_count == max_topics:
                max_teams += 1

    return (max_topics, max_teams)


assert acmTeam([
    "10101",
    "11100",
    "11010",
    "00101"
]) == (5, 2)

assert acmTeam([
    "11101",
    "10101",
    "11001",
    "10111",
    "10000",
    "01110"
]) == (5, 6)
