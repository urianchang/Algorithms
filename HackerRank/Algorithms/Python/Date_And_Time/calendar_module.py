# https://www.hackerrank.com/challenges/calendar-module/problem

import calendar

m, d, y = map(int, raw_input().strip().split())
print calendar.day_name[calendar.weekday(y, m, d)].upper()