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
    child_nodes = []

    for i in range(children):
        meta_total, node_value, data = parse(data)
        meta_totals += meta_total
        child_nodes.append(node_value)

    meta_totals += sum(data[:metas])

    if children == 0:
        return (
            meta_totals,
            sum(data[:metas]),
            data[metas:]
        )
    else:
        return (
            meta_totals,
            sum(
                child_nodes[i - 1] for i in data[:metas]
                if i > 0 and i <= len(child_nodes)
            ),
            data[metas:]
        )

total, root_value, _ = parse(file_data)
print(f"Part 1 - Metadata sum: {total}") # 45194
print(f"Part 2 - Value of root node: {root_value}") # 22989
