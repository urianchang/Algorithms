# Python 3.7
# https://www.hackerrank.com/challenges/find-angle/problem
import math


ab = int(input())
bc = int(input())
hypot = math.hypot(ab, bc)
deg = round(math.degrees(math.acos(bc/hypot)))
print(f"{deg}{chr(176)}")
