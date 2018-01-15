"""
Sequence Equation

URL: https://www.hackerrank.com/challenges/permutation-equation/problem
"""
import sys

def permutationEquation(p):
    # Complete this function

if __name__ == "__main__":
    n = int(raw_input().strip())    # number of elements in the sequence
    p = map(int, raw_input().strip().split(' '))    # values of p(1),...,p(n)
    result = permutationEquation(p)
    print "\n".join(map(str, result))
