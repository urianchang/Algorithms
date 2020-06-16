# https://www.hackerrank.com/challenges/lisa-workbook/problem
import math
from typing import List

def workbook(n: int, k: int, arr: List[int]) -> int:
    """Lisa just got a new math workbook. A workbook contains exercise problems,
    grouped into chapters. Lisa believes a problem to be special
    if its index (within a chapter) is the same as the page number
    where it's located.

    :param n: number of chapters
    :param k: maximum number of problems
    :param arr: number of problems per chapter
    :return: number (int) of special problems in the workbook
    """
    cursor = 1
    count = 0
    for chapter, problems in enumerate(arr):
        chapter_pages = math.ceil(problems / k)
        end = cursor + chapter_pages - 1
        # print(f"chap: {chapter}, start: {cursor}, end: {end}")
        plist = list(range(1, problems+1))
        pcur = 0
        for page in range(cursor, end+1):
            pslice = plist[pcur:pcur+k]
            count += 1 if page in pslice else 0
            pcur += k
        cursor = end + 1

    return count

assert workbook(5, 3, [4, 2, 6, 1, 10]) == 4
assert workbook(10, 5, [3, 8, 15, 11, 14, 1, 9, 2, 24, 31]) == 8
