# https://www.hackerrank.com/challenges/circular-array-rotation/problem

# Complete the circularArrayRotation function below.
def circularArrayRotation(a, k, queries):
    d = {}
    for i, v in enumerate(a):
        pos = (i + k) % len(a)
        d[pos] = v
    return [d[q] for q in queries]


assert circularArrayRotation([1, 2, 3], 2, [0, 1, 2]) == [2, 3, 1]
