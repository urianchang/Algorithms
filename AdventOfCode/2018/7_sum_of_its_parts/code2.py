# Python 3.7
from collections import defaultdict
import heapq

FILE = "input.txt"
NUM_ELVES = 5

leads_to = defaultdict(list)    # Steps that the step leads to
prereqs = defaultdict(list)     # Steps that need to be completed before the step


class Elf(object):
    def __init__(self):
        self.task = None        # type: string
        self.done = False       # type: boolean
        self.working_for = 0    # type: int

    def set_task(self, task):
        self.task = task
        self.done = False
        self.working_for = (ord(task) - ord('A') + 1) + 60

    def is_busy(self):
        return self.working_for > 0

    def work(self):
        if self.is_busy():
            self.working_for -= 1
            if self.working_for == 0:
                self.done = True


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

steps = []
workers = [Elf() for _ in range(NUM_ELVES)]
seconds_elapsed = 0

# Based on part 1, there are 26 possible steps
while len(steps) != 26:
    free_workers = [worker for worker in workers if not worker.is_busy()]

    # Assign work to free workers
    for worker in free_workers:
        if pq:
            next_task = heapq.heappop(pq)
            worker.set_task(next_task)

    # Put elves to work
    for worker in workers:
        worker.work()
        if worker.done:
            steps.append(worker.task)

            # Add the next step
            for possible_step in leads_to[worker.task]:
                prereq = prereqs[possible_step]
                if possible_step not in steps and all(p in steps for p in prereq):
                    heapq.heappush(pq, possible_step)

            worker.done = False
    seconds_elapsed += 1

print(f"Time to completion: {seconds_elapsed} seconds") # 1265
