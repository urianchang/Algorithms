# https://www.hackerrank.com/challenges/python-time-delta/problem

from datetime import datetime, timedelta

for _ in range(int(raw_input())):
    time_string1 = raw_input()
    t1 = datetime.strptime(time_string1[:-6], "%a %d %b %Y %H:%M:%S")
    op1 = time_string1[-5:][0]
    tz1 = time_string1[-4:]
    if op1 == "-":
        t1 += timedelta(hours=int(tz1[:2]), minutes=int(tz1[2:]))
    else:
        t1 -= timedelta(hours=int(tz1[:2]), minutes=int(tz1[2:]))

    time_string2 = raw_input()
    t2 = datetime.strptime(time_string2[:-6], "%a %d %b %Y %H:%M:%S")
    op2 = time_string2[-5:][0]
    tz2 = time_string2[-4:]
    if op2 == "-":
        t2 += timedelta(hours=int(tz2[:2]), minutes=int(tz2[2:]))
    else:
        t2 -= timedelta(hours=int(tz2[:2]), minutes=int(tz2[2:]))

    print int(abs((t1-t2).total_seconds()))
