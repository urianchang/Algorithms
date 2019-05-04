# Python 3.7
"""
Every instruction consists of four values: an opcode, two inputs (named A and
B), and an output (named C), in that order. The opcode specifies the behavior of
the instruction and how the inputs are interpreted. The output, C, is always
treated as a register.
"""
import copy
from collections import Counter, defaultdict


def addr(ins, reg):
    op, a, b, c = ins
    reg[c] = reg[a] + reg[b]
    return reg


def addi(ins, reg):
    # type: (list, list) -> list
    op, a, b, c = ins
    reg[c] = reg[a] + b
    return reg


def mulr(ins, reg):
    op, a, b, c = ins
    reg[c] = reg[a] * reg[b]
    return reg


def muli(ins, reg):
    op, a, b, c = ins
    reg[c] = reg[a] * b
    return reg


def banr(ins, reg):
    op, a, b, c = ins
    reg[c] = reg[a] & reg[b]
    return reg


def bani(ins, reg):
    op, a, b, c = ins
    reg[c] = reg[a] & b
    return reg


def borr(ins, reg):
    op, a, b, c = ins
    reg[c] = reg[a] | reg[b]
    return reg


def bori(ins, reg):
    op, a, b, c = ins
    reg[c] = reg[a] | b
    return reg


def setr(ins, reg):
    op, a, b, c = ins
    reg[c] = reg[a]
    return reg


def seti(ins, reg):
    op, a, b, c = ins
    reg[c] = a
    return reg


def gtir(ins, reg):
    op, a, b, c = ins
    reg[c] = 1 if a > reg[b] else 0
    return reg


def gtri(ins, reg):
    op, a, b, c = ins
    reg[c] = 1 if reg[a] > b else 0
    return reg


def gtrr(ins, reg):
    op, a, b, c = ins
    reg[c] = 1 if reg[a] > reg[b] else 0
    return reg


def eqir(ins, reg):
    op, a, b, c = ins
    reg[c] = 1 if a == reg[b] else 0
    return reg


def eqri(ins, reg):
    op, a, b, c = ins
    reg[c] = 1 if reg[a] == b else 0
    return reg


def eqrr(ins, reg):
    op, a, b, c = ins
    reg[c] = 1 if reg[a] == reg[b] else 0
    return reg


INSTR = {
    "addr": {"func": addr, "ops": [], "op": 0},
    "addi": {"func": addi, "ops": [], "op": 0},
    "mulr": {"func": mulr, "ops": [], "op": 0},
    "muli": {"func": muli, "ops": [], "op": 0},
    "banr": {"func": banr, "ops": [], "op": 0},
    "bani": {"func": bani, "ops": [], "op": 0},
    "borr": {"func": borr, "ops": [], "op": 0},
    "bori": {"func": bori, "ops": [], "op": 0},
    "setr": {"func": setr, "ops": [], "op": 0},
    "seti": {"func": seti, "ops": [], "op": 0},
    "gtir": {"func": gtir, "ops": [], "op": 0},
    "gtri": {"func": gtri, "ops": [], "op": 0},
    "gtrr": {"func": gtrr, "ops": [], "op": 0},
    "eqir": {"func": eqir, "ops": [], "op": 0},
    "eqri": {"func": eqri, "ops": [], "op": 0},
    "eqrr": {"func": eqrr, "ops": [], "op": 0}
}

FILE = 'input.txt'

codes = defaultdict(set)
tally = 0
executions = []
lines = open(FILE, 'r').readlines()
for i in range(0, len(lines), 4):
    if lines[i].startswith("Before"):
        before = list(map(int, lines[i].strip().split('[')[1].rstrip(']').split(',')))
        ex = list(map(int, lines[i+1].strip().split()))
        after = list(map(int, lines[i+2].strip().split('[')[1].rstrip(']').split(',')))

        matches = 0
        for ins in INSTR:
            b = copy.copy(before)
            tentative = INSTR[ins]['func'](ex, b)
            if tentative == after:
                INSTR[ins]['ops'].append(ex[0])
                codes[ex[0]].add(ins)
                matches += 1

        if matches >= 3:
            tally += 1
    else:
        executions.extend([
            list(map(int, line.strip().split()))
            for line in lines[i:i+4] if line.strip()
        ])

print(f"Part 1 - Samples like 3+ opcodes: {tally}") # 646

# Find which opcode goes with which function using process of elimination
code_map = {}
while len(code_map) != 16:
    for code, values in codes.items():
        if len(values) == 1:
            the_one = values.pop()
            code_map[code] = the_one
            for c in codes.keys():
                if the_one in codes[c]:
                    codes[c].remove(the_one)


the_reg = [0, 0, 0, 0]
for execution in executions:
    op = execution[0]
    the_reg = INSTR[code_map[op]]['func'](execution, the_reg)

print(f"Part 2 - Value @ register 0: {the_reg[0]}")