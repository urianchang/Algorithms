# https://www.hackerrank.com/challenges/append-and-delete/problem

def appendAndDelete(s: str, t: str, k: int) -> str:
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
    # Find parts of the strings that are common
    common = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            common += 1
        else:
            break

    diff_s = len(s) - common
    diff_t = len(t) - common

    if (diff_s + diff_t) > k:
        # We need more moves to account for all the differences
        return "No"
    elif (diff_s + diff_t)%2 == k%2:
        # If we have an even number of differences,
        # we need an even number of moves (and vice versa)
        return "Yes"
    elif (len(s) + len(t) - k) < 0:
        # If we completely delete the word, we can allow for a lot more moves
        return "Yes"
    else:
        return "No"


assert appendAndDelete("hackerhappy", "hackerrank", 9) == "Yes"
assert appendAndDelete("aba", "aba", 7) == "Yes"
assert appendAndDelete("ashley", "ash", 2) == "No"
