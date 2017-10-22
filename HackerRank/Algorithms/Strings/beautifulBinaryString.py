"""
Beautiful Binary String:

Alice has a binary string, B, of length n. She thinks a binary string is
beautiful if and only if it doesn't contain the substring "010".

In one step, Alice can change a 0 to a 1 (or vice-versa). Count and print the
minimum number of steps needed to make Alice see the string as beautiful.
"""

n = int(raw_input().strip())
B = raw_input().strip()

print B.count("010")

"""
Input:
7
0101010

Output:
2
"""
