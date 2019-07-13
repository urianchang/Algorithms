# Python 3
# https://www.hackerrank.com/challenges/ginorts/problem

# Given a string S:
#   * All sorted lowercase letters are ahead of uppercase letters.
#   * All sorted uppercase letters are ahead of digits.
#   * All sorted odd digits are ahead of sorted even digits.

S = input()

lower_case = []
upper_case = []
even_digits = []
odd_digits = []

for char in S:
    if char.islower():
        lower_case.append(char)
    elif char.isupper():
        upper_case.append(char)
    else:
        if int(char) % 2 == 0:
            even_digits.append(char)
        else:
            odd_digits.append(char)

lower_case.sort()
upper_case.sort()
even_digits.sort()
odd_digits.sort()

lower_case = ''.join(lower_case)
upper_case = ''.join(upper_case)
digits = ''.join(odd_digits) + ''.join(even_digits)

print(f"{lower_case}{upper_case}{digits}")
