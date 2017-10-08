"""
Caesar Cipher:

Julius Caesar protected his confidential information by encrypting it in a
cipher. Caesar's cipher rotated every letter in a string by a fixed number,
K, making it unreadable by his enemies. Given a string, S, and a number, K,
encrypt S and print the resulting string.

NOTE: The cipher only encrypts letters; symbols, such as -, remain unencrypted.
"""

N = int(raw_input().strip()) # length of string
S = raw_input().strip() # string
K = int(raw_input().strip())    # encryption key

'''
ASCII characters:
A-Z: 65 - 90
a-z: 97 - 122
'''

converted = ""
for ch in S:
    code = ord(ch)
    if code >= 65 and code <= 90:
        code += K
        while code > 90:
            code = (code - 90) + 64
    if code >= 97 and code <= 122:
        code += K
        while code > 122:
            code = (code - 122) + 96
    converted += chr(code)

print converted

"""
Input:
11
middle-Outz
2

Output:
okffng-Qwvb

"""
