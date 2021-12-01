example_1 = """\
199
200
208
210
200
207
240
269
260
263"""

with open("./inputs/01_sonar_sweep.txt", 'r') as fs:
    data1 = fs.read()

# PART 1
def solve(data: str):
    depths = data.strip().split()
    count = 0
    for i in range(1, len(depths)):
        if int(depths[i]) > int(depths[i-1]):
            count += 1
    return count


assert solve(example_1) == 7
print(solve(data1))  # 1521


# PART 2
def solve2(data: str):
    depths = [int(p) for p in data.strip().split()]
    count = 0
    for i in range(4, len(depths)+1):
        a = depths[i-4:i-1]
        b = depths[i-3:i]
        if sum(b) > sum(a):
            count += 1
    return count


assert solve2(example_1) == 5
print(solve2(data1))  # 1543
