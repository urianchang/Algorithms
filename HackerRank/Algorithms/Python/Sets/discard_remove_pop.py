# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

n = int(raw_input().strip())
s = set(map(int, raw_input().strip().split()))
N = int(raw_input().strip())

for _ in range(N):
    op = raw_input()
    if op.startswith('p'):
        try:
            s.pop()
        except KeyError:
            continue
    elif op.startswith('r'):
        val = int(op.split()[1])
        try:
            s.remove(val)
        except KeyError:
            continue
    else:
        val = int(op.split()[1])
        s.discard(val)

print sum(s)
