# https://www.hackerrank.com/challenges/re-split/problem
import re

regex_pattern = r"[,\.]"	# Do not delete 'r'.
print("\n".join(re.split(regex_pattern, raw_input())))
