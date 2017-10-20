"""
Designer PDF Viewer

When you select a contiguous block of text in a PDF viewer, the selection is
highlighted with a blue rectangle. In a new kind of PDF viewer, the selection
of each word is independent of the other words; this means that each rectangular
selection area forms independently around each highlighted word.

In this type of PDF viewer, the width of the rectangular selection area is equal
to the number of letters in the word times the width of a letter, and the height
is the maximum height of any letter in the word.

Consider a word consisting of lowercase English alphabetic letters, where each
letter is 1 mm wide. Given the height of each letter in millimeters (mm), find
the total area that will be highlighted by blue rectangle in mm^2 when the given
word is selected in our new PDF viewer.
"""
import sys

h = map(int, raw_input().strip().split(' '))    # heights of letters
word = raw_input().strip()

# Use ord to find unicode code for character(s)
maxHeight = max(h[ord(ch)-ord('a')] for ch in word)
print maxHeight * len(word)

# Make it a one-liner
# print max(h[ord(ch)-ord('a')] for ch in word) * len(word)
