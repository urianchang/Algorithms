"""
Missing Numbers

URL: https://www.hackerrank.com/challenges/missing-numbers/problem
"""
import sys

def missingNumbers(arr, brr):
    # type: (list, list) -> list
    minimum = min(min(arr), min(brr))
    maximum = max(max(arr), max(brr))
    cache = [0] * (maximum-minimum+1)
    for n in brr:
        cache[n-minimum] += 1
    for n in arr:
        cache[n-minimum] -= 1
    result = []
    for i in xrange(len(cache)):
        if cache[i] != 0:
            result.append(i+minimum)
    return result


if __name__ == "__main__":
    n = int(raw_input().strip())    # size of the first list
    arr = map(int, raw_input().strip().split(' '))  # first list
    m = int(raw_input().strip())    # size of the second list
    brr = map(int, raw_input().strip().split(' '))  # second list
    result = missingNumbers(arr, brr)
    print " ".join(map(str, result))
