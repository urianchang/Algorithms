"""
Sock Merchant:

John's clothing store has a pile of n loose socks where each sock, i, is
labeled with an integer, c, denoting its color. He wants to sell as many
socks as possible, but his customers will only buy them in matching pairs.
Two socks, i and j, are a single matching pair if they have the same color.

Given n and the color of each sock, how many pairs of socks can John sell?
"""

n = int(raw_input().strip())
socks = raw_input().strip().split()
socksHash = {}

for sock in socks:
    if socksHash.get(sock):
        socksHash[sock] += 1
    else:
        socksHash[sock] = 1

pairs = 0
for value in socksHash.values():
    pairs += int(int(value)/2)

print pairs

"""
Sample Input:
9
10 20 20 10 10 30 50 10 20

Sample Output:
3
"""
