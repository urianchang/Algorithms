"""
String Validators

https://www.hackerrank.com/challenges/string-validators/problem
"""
S = raw_input()

print any(c.isalnum() for c in S)
print any(c.isalpha() for c in S)
print any(c.isdigit() for c in S)
print any(c.islower() for c in S)
print any(c.isupper() for c in S)
