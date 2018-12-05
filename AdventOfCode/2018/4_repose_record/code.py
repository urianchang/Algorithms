# Python 3.7
from collections import Counter
from datetime import datetime

# Create list of tuple(datetime, str)
ls = []
with open('input.txt', 'r') as fh:
    for line in fh:
        log_parts = line.strip().split(']')
        log_date = datetime.strptime(
            log_parts[0].lstrip('['),
            "%Y-%m-%d %H:%M"
        )
        ls.append((log_date, log_parts[1].strip()))

# Keep track of guard's sleep patterns
sleep_start = None
guards = {}
for entry in sorted(ls, key=lambda p: p[0]):
    if entry[1].startswith("Guard"):
        current_guard = int(entry[1].split(' ')[1].lstrip("#"))
    elif entry[1].startswith("falls"):
        sleep_start = entry[0]
    elif entry[1].startswith("wakes"):
        sleep_dur = int((entry[0] - sleep_start).total_seconds()/60)
        if current_guard in guards:
            guards[current_guard]['time_slept'] += sleep_dur
            guards[current_guard]['sleep_minutes'].append(sleep_start.minute)
            guards[current_guard]['sleep_times'].append((sleep_start.minute, entry[0].minute))
        else:
            guards[current_guard] = {
                'time_slept': sleep_dur,
                'sleep_minutes': [sleep_start.minute],
                'sleep_times': [(sleep_start.minute, entry[0].minute)]
            }

# Part 1: Find the guard that sleeps the most
most_sleepy = None
for guard, meta in guards.items():
    if most_sleepy is None:
        most_sleepy = guard
    elif meta['time_slept'] > guards[most_sleepy]['time_slept']:
        most_sleepy = guard

minute = Counter(guards[most_sleepy]['sleep_minutes']).most_common(1)[0][0]
print(most_sleepy * minute)   # 94040

# Part 2: Find the guard that sleeps the most in the same minute
(guard, minute, count) = max(
    [
        (guard, minute, sum(
            1 for start, end in guards[guard]['sleep_times']
            if start <= minute < end)
        ) for minute in range(60) for guard in guards],
    key=lambda i: i[2])
print(guard * minute)   # 39940
