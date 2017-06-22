# Grading Students
import sys
import math

def solve(grades):
    # Complete this function
    arr = []
    for i in range(len(grades)):
        m = math.ceil(grades[i]/5.0)
        # print "m", m
        if grades[i] < 38:
            arr.append(grades[i])
            continue
        if int(m*5) - grades[i] < 3:
            arr.append(int(m*5))
        else:
            arr.append(grades[i])
            # print grades[i]
    return arr

n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)
result = solve(grades)
print "\n".join(map(str, result))
