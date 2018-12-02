# Python 3.7
from collections import Counter

# Part 1
twice = 0
thrice = 0
with open('input.txt', 'r') as fh:
    for id in fh:
        if len(set(id)) != len(id):
            counts = Counter(list(id)).values()
            if 2 in counts:
                twice += 1
            if 3 in counts:
                thrice += 1

checksum = twice * thrice
print(checksum) # 5000

# Part 2
with open('input.txt', 'r') as fh:
    id_list = fh.read().strip().splitlines()

is_done = False
for i in id_list:
    for j in id_list:
        diffs = 0
        for pair in zip(list(i), list(j)):
            if pair[0] != pair[1]:
                diffs += 1
        if diffs == 1:
            ans = [ch for idx, ch in enumerate(i) if j[idx] == ch]
            print(''.join(ans)) # ymdrchgpvwfloluktajxijsqb
            is_done = True
            break
    if is_done:
        break
