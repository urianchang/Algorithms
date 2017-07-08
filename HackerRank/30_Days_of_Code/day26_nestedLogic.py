"""
Day 26: Nested Logic

Given expected and actual return dates for a library book,
create a program that calculates the fee structure.
"""

# inputs will come in 'day, month, year'
ad, am, ay = [ int(x) for x in raw_input().strip().split() ]
ed, em, ey = [ int(x) for x in raw_input().strip().split() ]

if ay > ey:
    print (10000)
elif ay == ey and am > em:
    print ((am - em) * 500)
elif ay == ey and am == em and ad > ed:
    print ((ad - ed) * 15)
else:
    print (0)
