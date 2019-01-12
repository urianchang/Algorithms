# https://www.hackerrank.com/challenges/validating-uid/problem
"""
Valid UID:

- at least 2 uppercase English alphabet characters
- at least 3 digits (0 - 9)
- only alphanumeric characters (a-z, A-Z, 0-9)
- No repeating characters
- Exactly 10 characters
"""
import re

for _ in range(int(raw_input().strip())):
    UID = raw_input().strip()
    try:
        assert len(set(UID)) == len(UID)
        assert re.search(r"[a-zA-Z0-9]{10}", UID)
        assert len(re.findall(r"[0-9]", UID)) >= 3
        assert len(re.findall(r"[A-Z]", UID)) >= 2
        print "Valid"
    except:
        print "Invalid"
