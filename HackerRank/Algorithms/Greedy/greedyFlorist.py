# https://www.hackerrank.com/challenges/greedy-florist/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms


def getMinimumCost(k, c):
    t = 0
    count = 1
    c.sort()
    print(c[:-k])
    while len(c) > 0:
        t += sum(c[-k:]) * count
        del c[-k:]
        count += 1
    return t


assert getMinimumCost(2, [2, 5, 6]) == 15
assert getMinimumCost(3, [2, 5, 6]) == 13
assert getMinimumCost(3, [1, 3, 5, 7, 9]) == 29
