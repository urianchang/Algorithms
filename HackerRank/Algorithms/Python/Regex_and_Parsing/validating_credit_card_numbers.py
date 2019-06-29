# Python 3.7
# https://www.hackerrank.com/challenges/validating-credit-card-number/problem
import re

for _ in range(int(input())):
    card = input().strip()
    if re.compile(r'^(?:.{4}\-){3}.{4}$').match(card):
        card = card.replace('-', '')
    if re.compile(r'^[456]\d{15}$').match(card) and \
        not re.compile(r'(.)\1{3}').search(card):
        print('Valid')
    else:
        print('Invalid')
