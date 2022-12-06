# https://leetcode.com/problems/decode-ways/


def numDecodings(s: str) -> int:
    # Time: O(n) | Space: O(n)
    # Recursive tree, bottom up dynamic programming
    # https://www.youtube.com/watch?v=Km4iqih6WjI

    # Keep track of previous legitimate combinations
    register = [0] * (len(s)+1)
    register[0] = 1
    register[1] = 0 if s[0] == "0" else 1

    # Start decoding by looking back for valid single and double digits
    for i in range(2, len(s)+1):
        single = int(s[i-1:i])
        double = int(s[i-2:i])
        if single >= 1:
            register[i] += register[i-1]
        if 10 <= double <= 26:
            register[i] += register[i-2]

    return register[len(s)]


assert numDecodings("12") == 2
assert numDecodings("226") == 3
assert numDecodings("06") == 0
