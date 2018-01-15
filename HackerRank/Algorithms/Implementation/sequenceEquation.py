"""
Sequence Equation

URL: https://www.hackerrank.com/challenges/permutation-equation/problem
"""
import sys

# Attempt 1: Created dictionary -- Passed 5/10
# def permutationEquation(p):
#     # Create dictionary with p(x) as key and index as value
#     d = {x:i for i, x in enumerate(p, start=1)}
#     # Return list created by getting key for each el of p in d
#     # and finding relative val in p
#     return [ p[d[i]-1] for i in p ]

# Attempt 2 -- Passed 10/10
def permutationEquation(p):
    # For each index in p, look for index of val in p and find index of index
    # x -> p(val) -> p(p(val))
    return [ p.index(p.index(i+1)+1)+1 for i in xrange(len(p)) ]

if __name__ == "__main__":
    n = int(raw_input().strip())    # number of elements in the sequence
    p = map(int, raw_input().strip().split(' '))    # values of p(1),...,p(n)
    result = permutationEquation(p)
    print "\n".join(map(str, result))

"""
Sample input:
3
2 3 1

Sample output:
2
3
1
"""
