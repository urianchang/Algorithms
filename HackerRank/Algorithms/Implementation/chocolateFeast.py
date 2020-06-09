# https://www.hackerrank.com/challenges/chocolate-feast/problem

def chocolateFeast(n: int, c: int, m: int) -> int:
    """Calculate how many chocolates can be eaten by Bobby

    :param n: initial amount of money
    :param c: cost of a chocolate bar
    :param m: number of wrappers that can be turned in for a free bar
    :return: Total number of chocolates that can be bought
    """
    bars = n // c
    wrappers = bars
    while (wrappers >= m):
        exchanged = wrappers // m
        bars += exchanged
        leftover = wrappers % m
        wrappers = exchanged + leftover

    return bars


assert chocolateFeast(10, 2, 5) == 6
assert chocolateFeast(12, 4, 4) == 3
assert chocolateFeast(6, 2, 2) == 5
assert chocolateFeast(15, 3, 2) == 9
