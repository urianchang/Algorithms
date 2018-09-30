# https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem

import re

print sorted(list(
    filter(
        lambda email: re.match(r"[\w-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$", email),
        list(
            raw_input().strip() for _ in range(int(raw_input().strip()))
        )
    )
))
