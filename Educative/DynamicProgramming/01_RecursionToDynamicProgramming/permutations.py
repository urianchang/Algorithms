# Find all permutations of a string
from typing import List


def permutations(s: str) -> List[str]:
    if s == "":
        return [""]
    permutes = []
    for char in s:
        subpermutes = permutations(s.replace(char, "", 1))  # recursive step
        for suffix in subpermutes:
            permutes.append(char + suffix)
    return permutes


print(permutations("abcd"))
