# https://leetcode.com/problems/longest-palindromic-substring/


def longestPalindrome_slow(s: str) -> str:
    # This solution is TOO SLOW
    # Given a string s, find the longest palindromic substring in s.
    # You may assume that the maximum length of s is 1000.
    palindromes = []

    # Find all matching characters
    chars = {}
    for i in range(len(s)):
        char = s[i]
        if char not in chars:
            chars[char] = [i]
        else:
            chars[char].append(i)

    # Find palindromes
    s_list = list(s)
    for matches in chars.values():
        if len(matches) < 2:
            continue

        for i in range(len(matches)-1):
            for j in range(i+1, len(matches)):
                forward = s_list[matches[i]:matches[j]+1]
                reverse = forward[::-1]
                if forward == reverse:
                    palindromes.append("".join(forward))

    # Find longest palindrome
    longest = s[0]
    for p in palindromes:
        if len(p) > len(longest):
            longest = p

    return longest


def longestPalindrome(s: str) -> str:
    def palindrome(string: str, left: int, right: int) -> str:
        # It's faster to build palindromes on top of an existing one
        while left >= 0 and right < len(string) and string[left] == string[right]:
            left -= 1
            right += 1
        return string[left+1:right]

    longest = ""
    for i in range(len(s)):
        odd = palindrome(s, i, i)
        even = palindrome(s, i, i+1)

        longest = max(longest, odd, even, key=len)

    return longest


assert longestPalindrome("cbbd") == "bb"
assert longestPalindrome("babad") in ("aba", "bab")
assert longestPalindrome("a") == "a"
