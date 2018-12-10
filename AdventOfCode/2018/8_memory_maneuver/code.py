# Python 3.7
"""
Specifically, a node consists of:

- A header, which is always exactly two numbers:
    - The quantity of child nodes.
    - The quantity of metadata entries.
- Zero or more child nodes (as specified in the header).
- One or more metadata entries (as specified in the header).
"""

file = 'input.txt'
file_data = list(map(int, open(file, 'r').read().strip().split()))


def parse(data):
    children, metas = data[:2]
    data = data[2:]
    meta_totals = 0

    # print(f"c: {children}, m: {metas}, d: {data}")

    for i in range(children):
        meta_total, data = parse(data)
        meta_totals += meta_total

    meta_totals += sum(data[:metas])
    return (meta_totals, data[metas:])

meta_sum, remaining = parse(file_data)
print(f"Part 1 - Metadata sum: {meta_sum}") # 45194
