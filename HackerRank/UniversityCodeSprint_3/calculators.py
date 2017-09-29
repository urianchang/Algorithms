"""
A Small Step Toward Calculators

Alice has a string of the form 'x+y' or 'x-y'. 'x' and 'y' are single-digit
nonnegative integers. Her task is to perform the addition or subtraction
accordingly and print the result.

As a newbie programmer, Alice is struggling to finish the task. Can you
help her?
"""

import sys

def solve(opr):
    # Complete this function
    if opr[1] == "+":
        return int(opr[0]) + int(opr[2])
    elif opr[1] == "-":
        return int(opr[0]) - int(opr[2])
    else:
        return "Operand not supported"

if __name__ == "__main__":
    opr = raw_input().strip()
    result = solve(opr)
    print result

"""
Sample Input:
0+1

Sample Output:
1
"""
