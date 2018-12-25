# https://www.hackerrank.com/challenges/polar-coordinates/problem
"""
cmath.phase
This tool returns the phase of complex number 'z' (a.k.a. argument of 'z')

abs
This tool returns the modulus (absolute value) of complex number 'z'
"""
import cmath

z = complex(raw_input().strip())
print(abs(z))           # Value of modulus
print(cmath.phase(z))   # Value of phase angle
