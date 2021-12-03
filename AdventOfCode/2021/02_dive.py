
example1 = """\
forward 5
down 5
forward 8
up 3
down 8
forward 2"""


# PART 1
def solve1(ip: str):
    x = 0
    y = 0
    for d in ip.split("\n"):
        move, unit = d.split(" ")
        if move == "forward":
            x += int(unit)
        elif move == "up":
            y -= int(unit)
        else:  # Else: down
            y += int(unit)
    return x*y


assert solve1(example1) == 150

with open("./inputs/02_dive.txt", "r") as fs:
    data = fs.read()

print(solve1(data))  # 1488669

# PART 2
def solve2(ip: str):
    x = 0
    y = 0
    aim = 0
    for d in ip.split("\n"):
        move, unit = d.split(" ")
        unit = int(unit)
        if move == "forward":
            x += unit
            y += (aim * unit)
        elif move == "up":
            aim -= unit
        else:  # Else: down
            aim += unit
    return x*y


assert solve2(example1) == 900
print(solve2(data))  # 1176514794
