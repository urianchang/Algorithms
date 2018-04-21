"""
Strong Password

URL: https://www.hackerrank.com/challenges/strong-password/problem
"""
special_characters = "!@#$%^&*()-+"

n = int(raw_input().strip())
pw = raw_input().strip()
errs = 0

if any(c.isdigit() for c in pw) == False:
    errs += 1
if any(c.islower() for c in pw) == False:
    errs += 1
if any(c.isupper() for c in pw) == False:
    errs += 1
if any(c in special_characters for c in pw) == False:
    errs += 1
print max(errs, 6-n)
