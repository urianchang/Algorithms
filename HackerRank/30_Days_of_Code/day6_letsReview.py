"""
Day 6: Let's Review

Given a string 'S' of length 'N' that is indexed from 0 to N - 1,
print its even-indexed and odd-indexed characters as 2 space-separated
strings on a single line. Note: '0' is considered to an even index.
"""

T = int(raw_input().strip())
for i in range(0, T):
    S = str(raw_input().strip())
    Se = ""
    So = ""
    for idx in range(len(S)):
        if idx%2 != 0:
            So += S[idx]
        else:
            Se += S[idx]
    print Se, So
