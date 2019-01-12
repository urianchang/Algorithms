# https://www.hackerrank.com/challenges/validate-a-roman-number/problem

import re

thousand = r"M{0,3}"
hundred = r"(C[MD]|D?C{0,3})"
ten = r"(X[CL]|L?X{0,3})"
ones = r"(I[VX]|V?I{0,3})"

print(bool(re.match(thousand+hundred+ten+ones+"$", raw_input().strip())))
