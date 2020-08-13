# https://leetcode.com/problems/most-common-word/
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        max_count = 0
        common_word = ""
        counts = defaultdict(int)

        buffer = []
        end = len(paragraph) - 1
        for i, ch in enumerate(paragraph):
            if ch.isalnum():
                buffer.append(ch.lower())
                if i != end:
                    continue

            if len(buffer) > 0:
                word = "".join(buffer)
                if word not in banned:
                    counts[word] += 1
                    if counts[word] > max_count:
                        max_count = counts[word]
                        common_word = word
                buffer = []

        return common_word

