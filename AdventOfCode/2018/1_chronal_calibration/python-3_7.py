# Python 3.7.0

# Part 1
freq = 0
with open('./input.txt', 'r') as f:
    for num in f:
        freq += int(num)

print(f"final frequency: {freq}")

# Part 2
f = 0
s = set()
i = 0

keep_going = True
while keep_going:
    with open('./input.txt', 'r') as fh:
        for num in fh:
            f += int(num)
            if f in s:
                print(f"first to twice: {f}")
                keep_going = False
                break
            else:
                s.add(f)
    i += 1

print(f"total iterations: {i}")
