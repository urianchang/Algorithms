"""
sWAP cASE

https://www.hackerrank.com/challenges/swap-case/problem
"""

def swap_case(s):
    return "".join(
        map(
            lambda x: x.lower() if x.isupper() else x.upper(),
            list(s)
        )
    )

print swap_case('AsDf')
print swap_case('HackerRank.com presents "Pythonist 2".')
