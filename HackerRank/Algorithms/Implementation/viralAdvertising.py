"""
Viral Advertising:

HackerLand Enterprise is adopting a new viral advertising strategy. When
they launch a new product, they advertise it to exactly 5 people on social
media.

On the first day, half of those 5 people like the advertisement and each
person shares it with 3 of their friends; the remaining people delete the
advertisement because it doesn't interest them. And so on.

Given an integer 'n' find and print the total number of people who liked
the advertisement during the first n days. It is guaranteed that no two
people have any friends in common and, after a person shares the ad with
a friend, the friend always sees it the next day.
"""

n = int(raw_input().strip())    # Number of days

fans = 5
likes = 0

for _ in xrange(n):
    likes += fans//2
    fans = (fans//2) * 3

print likes

"""
Input:
3

Output:
9
"""
