"""
Nested Lists

URL: https://www.hackerrank.com/challenges/nested-list/problem
"""

n = int(raw_input().strip())    # number of students
grades = [ [raw_input().strip(), float(raw_input().strip())] for _ in xrange(n)]

# Find the second lowest score
second_lowest = sorted(list(set(grade for name, grade in grades)))[1]

# Use list comprehension to create list of names with lowest score
print '\n'.join(sorted([name for name, grade in grades if grade == second_lowest]))
