# Python 3.7
# https://www.hackerrank.com/challenges/matrix-script/problem
import re
from typing import List


def decode_matrix(matrix: List[str], cols: int) -> str:
    # Alphanumeric characters consist of: [A-Z, a-z, and 0-9]
    decoded = ""
    for i in range(cols):
        for word in matrix:
            decoded += word[i]

    # Do lookbehind and lookahead
    mre = re.compile('(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])')
    return mre.sub(" ", decoded)


assert decode_matrix(["Tsi", "h%x", "i #", "sM ", "$a ", "#t%", "ir!"], 3) == "This is Matrix#  %!"


n, m = map(lambda x: int(x), input().strip().split())

matrix = []
for _ in range(n):
    matrix.append(input())

print(decode_matrix(matrix, m))