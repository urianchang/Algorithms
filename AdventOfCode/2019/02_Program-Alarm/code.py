import copy


def intcode(codes):
    cur = 0
    while codes[cur] != 99:
        group = codes[cur:cur+4]
        opcode = group[0]
        if opcode == 1:
            output = codes[group[1]] + codes[group[2]]
        else:   # opcode == 2
            output = codes[group[1]] * codes[group[2]]
        codes[group[3]] = output
        cur = cur+4
    return codes[0]

sample = [1,9,10,3,2,3,11,0,99,30,40,50]
assert intcode(sample) == 3500

inputs = []
with open('input.txt') as fh:
    inputs = [int(code) for code in fh.read().strip().split(',')]

# Part I:
input_1 = copy.copy(inputs)
input_1[1] = 12
input_1[2] = 2
p1 = intcode(input_1)
assert p1 == 3166704
print("1: {}".format(p1))

# Part II:
input_2 = copy.copy(inputs)
input_2[1] = 80
input_2[2] = 18
assert intcode(input_2) == 19690720
print("2: {}".format(100 * 80 + 18))
