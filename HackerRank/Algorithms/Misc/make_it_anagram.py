"""
Make It Anagram

URL: https://www.hackerrank.com/challenges/make-it-anagram-mglines/problem
"""

w1 = raw_input()
w2 = raw_input()

total = 0
for letter in "abcdefghijklmnopqrstuvwxyz":
    total += abs(w1.count(letter) - w2.count(letter))
print total
