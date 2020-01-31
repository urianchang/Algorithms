import math


masses = []
with open('input.txt') as fh:
    for mass_str in fh.readlines():
        mass = float(mass_str.strip())
        masses.append(mass)

total_p1 = 0
for mass in masses:
    fuel = math.floor(mass/3) - 2
    total_p1 += fuel

assert total_p1 == 3266053
print("Part 1: {}".format(int(total_p1)))

# For Part II:
def make_fuel(mass):
    fuel = math.floor(mass/3) - 2
    if fuel <= 0:
        return 0
    return fuel + make_fuel(fuel)


assert make_fuel(14) == 2
assert make_fuel(1969) == 966
assert make_fuel(100756) == 50346

total_p2 = 0
for mass in masses:
    total_p2 += make_fuel(mass)

assert total_p2 == 4896221.0
print("Part 2: {}".format(int(total_p2)))
