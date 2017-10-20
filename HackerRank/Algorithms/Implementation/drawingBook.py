"""
Drawing Book

Brie's Drawing teacher asks her class to open their n-page book to page number
p. Brie can either start turning pages from the front of the book or from the
back of the book, and she always turns pages one-by-one. When she opens the
book, page 1 is always on the right side.

Each page in the book has two sides, front and back, except for the last page
which may only have a front side depending on the total number of pages of the
book.

Given n and p, find and print the minimum number of pages Brie must turn in
order to arrive at page p.
"""
import sys

def solve(n, p):
    '''
    Since Python rounds down...
    Number of pages to turn to from front: p/2
    Number of pages to turn to from back: (n/2) - (p/2)
    '''
    return min(p/2, (n/2)-(p/2))

n = int(raw_input().strip())    # number of pages in the book
p = int(raw_input().strip())    # page to turn to
result = solve(n, p)
print(result)

"""
Input 0:
6
2

Output 0:
1

Input 1:
5
4

Output 1:
0
"""
