"""
Gemstones:

John has discovered various rocks. Each rock is composed of various elements,
and each element is represented by a lower-case Latin letter from 'a' to 'z'.
An element can be present multiple times in a rock. An element is called a
gem-element if it occurs at least once in each of the rocks.

Given the list of N rocks with their compositions, display the number of
gem-elements that exist in those rocks.
"""

N = int(raw_input().strip())

rocks = []

for _ in xrange(N):
    rocks.append(set(list(raw_input().strip())))

print len(set.intersection(*rocks))

"""
Input:
3
abcdde
baccd
eeabg

Output:
2
"""
