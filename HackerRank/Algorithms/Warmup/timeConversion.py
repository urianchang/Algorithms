"""
Time Conversion

Given a time in 12-hour AM/PM format,
convert it to military (24-hour) time.
"""

time = raw_input().strip().split(':')
# time = "07:45:15AM".strip().split(':')
if time[2][2:] == "AM":
    if time[0] == "12":
        time[0] = "00"
else:
    if time[0] != "12":
        time[0] = str(int(time[0]) + 12)
time[2] = time[2][:2]
print ":".join(time)
