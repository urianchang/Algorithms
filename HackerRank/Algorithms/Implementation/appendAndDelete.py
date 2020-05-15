# https://www.hackerrank.com/challenges/append-and-delete/problem

def appendAndDelete(s, t, k):
    """Determine if s can be converted into t in exactly k moves.

    There are only two types of moves:
        1. Append a letter to the end of the string.
        2. Delete the last character in the string.

    Args:
        s (str): initial string
        t (str): desired final string
        k (int): number of operations

    Returns:
        :str: "Yes", if "s" can be converted into "t"; otherwise, "No"
    """
    if s == t:
        if k >= 2:
            return "Yes"
        else:
            return "No"
    count = max(len(s), len(t))
    diff = 0
    for i in range(count):
        if i < (len(s) - 1):
            char1 = s[i]
            if i < (len(t) - 1):
                char2 = t[i]
                if char1 == char2:
                    continue
                else:
                    diff += 2
            else:
                diff += 1
        else:
            diff += 1





assert appendAndDelete("hackerhappy", "hackerrank", 9) == "Yes"
assert appendAndDelete("aba", "aba", 7) == "Yes"
assert appendAndDelete("ashley", "ash", 2) == "No"
