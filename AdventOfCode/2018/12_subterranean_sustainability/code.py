# Python 3.7
import copy
from pprint import pprint


def grow_once(plants, notebook):
    # type: (list, dict) -> list
    num_plants = len(plants)
    new_plants = copy.copy(plants)
    for p_idx in range(2, num_plants-2):
        combo = ''.join(plants[p_idx-2:p_idx+3])
        if combo in notes:
            # print(p_idx, combo)
            res = notes[combo]
            new_plants[p_idx] = res
        else:
            new_plants[p_idx] = '.'
    return new_plants


def growth_for(num_years, tunnel, notes, debug=False):
    # type: (int, list, dict) -> list
    t = tunnel
    growth_tracker = {0: count_plants(tunnel, length)}
    for i in range(1, num_years+1):
        t = grow_once(t, notes)
        if debug:
            num_plants = count_plants(t, length)
            growth_tracker[i] = num_plants
            diff = num_plants - growth_tracker[i-1]
            print(f"Gen {i}: {diff}")
    return t


def count_plants(tunnel, section_length):
    # type: (list, int) -> int
    total = 0
    for idx, pot in enumerate(tunnel):
        if pot == "#":
            total += idx - section_length
    return total


FILE = 'input.txt'
initial_state = []
notes = {}
with open(FILE, 'r') as fh:
    for line in fh:
        if line.startswith('initial'):
            initial_state.extend([
                plant for plant in line.strip().split(':')[1].strip()
            ])
        else:
            note = line.strip()
            if note:
                combo, res = note.split(' => ')
                notes[combo] = res

length = len(initial_state) * 10
tunnel = (['.'] * length) + initial_state + (['.'] * length)
# tunnel_now = growth_for(20, tunnel, notes)
# plants = count_plants(tunnel_now, length)
# print(f"Part 1 - Number of plants @ gen20: {plants}")    # 1672

# Part 2: Plants at generation 50_000_000_000 (50bn)

# Is there a pattern?
tunnel_now = growth_for(200, tunnel, notes, debug=False)
_200 = count_plants(tunnel_now, length)
# After generation 159, an additional 33 plants are added every year
_50bn = (50_000_000_000 - 200) * 33 + _200
print(f"Part 2 - Number of plants @ gen50bn: {_50bn}")  # 1650000000055
