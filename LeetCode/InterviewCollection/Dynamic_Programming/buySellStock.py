# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/572/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        min_price = prices[0]
        max_profit = 0
        for p in prices:
            min_price = min(p, min_price)
            profit = p - min_price
            max_profit = max(profit, max_profit)
        return max_profit
