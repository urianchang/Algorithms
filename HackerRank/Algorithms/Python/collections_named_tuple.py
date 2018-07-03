from collections import namedtuple

N = int(raw_input())
Student = namedtuple('Student', raw_input())
avg = sum(
    [float(Student(*raw_input().split()).MARKS)
     for _ in range(N)]
) / N
print "%.2f" % avg
