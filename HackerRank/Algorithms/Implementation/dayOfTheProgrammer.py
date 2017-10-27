"""
Day of the Programmer:

Marie invented a Time Machine and wants to test it by time-traveling to visit
Russia on the Day of the Programmer (256th day of the year) during a year in
the inclusive range from 1700 to 2700.

From 1700 to 1917, Russia's official calendar was the Julian calendar; since
1919 they used the Gregorian calendar system. The transition from the Julian
to the Gregorian calendar system occurred in 1918, when the next day after
January 31st was February 14th. This means that in 1918, February 14th was
the 32nd day of the year in Russia.

In both calendar systems, February is the only month with a variable amount of
days; it has 29 days during a leap year, and 28 days during all other years. In
the Julian calendar, leap years are divisible by 4; in the Gregorian calendar,
lead years are either of the following:
    * Divisible by 400
    * Divisible by 4 and not divisible by 100.

Given a year, y, find the date of the 256th day of the year according to the
official Russian calendar during that year. Print in the format, dd.mm.yyyy.
"""
import sys

def solve(year):
    isLeap = False
    if year == 1918:
        # End of Feb: 47th day of year (leap)
        return '26.09.1918'
    # Julian calendar
    if year <= 1917 and year >= 1700:
        if year%4 == 0:
            isLeap = True
    # Gregorian calendar
    else:
        if year%400 == 0 or (year%4 == 0 and year%100 != 0):
            isLeap = True
    if isLeap:
        return '12.09.' + str(year)
    else:    
        return '13.09.' + str(year)

year = int(raw_input().strip())
result = solve(year)
print(result)

"""
Input 0:
2017

Output 0:
13.09.2017

Input 1:
2016

Output 1:
12.09.2016
"""
