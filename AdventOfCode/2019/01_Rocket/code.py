import math


total_fuel = 0
with open('input.txt') as fh:
    for mass_str in fh.readlines():
        mass = float(mass_str.strip())
        fuel = math.floor(mass/3) - 2
        total_fuel += fuel

print("Part 1: {}".format(int(total_fuel)))

