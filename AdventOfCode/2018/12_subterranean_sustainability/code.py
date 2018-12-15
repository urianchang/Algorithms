# Python 3.7
import copy
from pprint import pprint


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

# print(initial_state)
# pprint(notes)
width = len(initial_state)
tunnel = (['.'] * width) + initial_state + (['.'] * width)

def grow(plants, notebook):
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


# print(''.join(tunnel))

# gen = {0: sum([1 for pot in tunnel if pot == "#"])}
for i in range(1,21):
    tunnel = grow(tunnel, notes)
    # gen[i] = sum([1 for pot in tunnel if pot == "#"])

# print(''.join(tunnel))
# num = sum(gen.values())

total = 0
for idx, pot in enumerate(tunnel):
    if pot == "#":
        total += idx - width

print(f"Part 1 - Number of plants: {total}")    # 1672

