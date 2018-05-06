def solution(N):
    # write your code in Python 3.6
    binary_representation = bin(N)
    max_gap = 0
    gap = 0
    for i in list(str(binary_representation)[2:]):
        if i == '0':
            gap += 1
        else:
            max_gap = max(max_gap, gap)
            gap = 0
    return max_gap

print solution(15)
