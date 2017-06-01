"""
Birthday Cake Candles

Colleen is turning 'n' years old! She has 'n' candles of various
heights on her cake, and candle 'i' has height 'height'. Because
taller candles tower over the shorter ones, Colleen can only blow
out the tallest candles.

Given the height, for each individual candle, find and print the number
of candles she can successfully blow out.
"""

n = int(raw_input().strip())
height = map(int,raw_input().strip().split(' '))

dictionary = {}
for i in range(n):
    if height[i] in dictionary:
        dictionary[height[i]] += 1
    else:
        dictionary[height[i]] = 1

print max(list(dictionary.values()))
