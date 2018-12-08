# Python 3.7
from collections import defaultdict
import heapq

FILE = "input.txt"

leads_to = defaultdict(list)    # Steps that the step leads to
prereqs = defaultdict(list)     # Steps that need to be completed before the step

with open(FILE, 'r') as fh:
    for line in fh:
        words = line.split()
        one, two = words[1].strip(), words[7].strip()
        leads_to[one].append(two)
        prereqs[two].append(one)

# Find possible first steps (no prereqs) and add to priority queue (heap)
pq = []
possible_starters = set(leads_to.keys()) - set(prereqs.keys())
for s in possible_starters:
    heapq.heappush(pq, s)

# Add possible steps to the heap and iterate through it
steps = []
while pq:
    next_step = heapq.heappop(pq)
    steps.append(next_step)
    for possible_step in leads_to[next_step]:
        prereq = prereqs[possible_step]
        if possible_step not in steps and all(p in steps for p in prereq):
            heapq.heappush(pq, possible_step)

print(f"Part 1 - Order: {''.join(steps)}")  # GKCNPTVHIRYDUJMSXFBQLOAEWZ
