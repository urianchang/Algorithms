"""
Dynamic Array
"""

N, Q = map(int, raw_input().strip().split())
seqList = [ [] for i in range(N) ]
lastAnswer = 0
for i in range(Q):
    m, x, y = map(int, raw_input().strip().split())
    if m == 1:
        seqList[(x ^ lastAnswer)%N].append(y)
    else:
        seq = seqList[(x ^ lastAnswer)%N]
        lastAnswer = seq[y%len(seq)]
        print lastAnswer
