"""
Bonnie and Clyde:

Bonnie and Clyde have decided to meet at a restaurant
to have Sushi. The city is given in the form of an
undirected graph with 'n' nodes and 'm' edges (without
any parallel edges or self loops). Bonnie's house is located
at node 'u' and Clyde's house is located at node 'v'.
The famous restaurant Sushi Grand is located at node 'w'.

Your task is to find out if Bonnie and Clyde can meet at
Sushi Grand such that their path has no common node
other than the destination 'w'.
"""

import sys

class Node:
    def __init__(self, val):
        self.value = val
        self.connections = []
    def connect(self, node):
        self.connections.append(node)

def walk(node1, node2, arr):
    if len(node1.connections) == 1 and node1.connections[0].value == node2.value:
        return arr.append(node1.value)
    for i in len(node1.connections):
        walk(i, node2, arr)
    return arr

n, m, q = raw_input().strip().split(' ')
n, m, q = [int(n), int(m), int(q)]
for a0 in xrange(m):
    u, v = raw_input().strip().split(' ')
    u, v = [int(u), int(v)]
    nodeU = Node(u)
    nodeV = Node(v)
    NodeU.connect(NodeV)
    NodeV.connect(NodeU)

for a0 in xrange(q):
    u, v, w = raw_input().strip().split(' ')
    u, v, w = [int(u), int(v), int(w)]
    # pathsU = walk(
