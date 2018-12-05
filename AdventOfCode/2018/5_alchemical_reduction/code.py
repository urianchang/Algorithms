# Python 3.7

M = {}  # Map alphabet lower and upper cases
alpha = 'abcdefghijklmnopqrstuvwxyz'
for ch in alpha:
    M[ch.upper()] = ch.lower()
    M[ch.lower()] = ch.upper()

def polymerize(line: str) -> int:
    # Shortens string by removing uppercase-lowercase character pairs
    i = 0
    while True:
        current = line[i]
        ahead = line[i+1:]  # "" if no more
        if not ahead:
            break

        if current == M[ahead[0]]:
            # Remove the pair and re-evaluate
            line = line[:i] + ahead[1:]
            if i > 0:
                i -= 1
        else:
            i += 1
    return len(line)


DATA = open('input.txt').read().splitlines()[0] # load all into memory

# Part 1
print(polymerize(DATA))    # 10250

# Part 2
distinct = set(DATA.lower())    # Filter based on possible characters in string
lengths = []
for c in distinct:
    data = ''.join([char for char in DATA if char != c and char != M[c]])
    lengths.append(polymerize(data))

print(min(lengths)) # 6188