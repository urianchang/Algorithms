"""
Modified Subsequence Sum:

Assume we have a sequence of numbers 'a' and a positive integer 'k'. Let 'b' be
any subsequence of 'a'.

We define S(b) as follows:
    * Let S1(b) be the sum of the elements in b. Next for each 1 <= i <= m-1, we
        consider the terms b[i] and b[i+1].
    * Let d[i] denote the distance between these terms in the original sequence
        'a'. By this we mean if the terms b[i] and b[i+1] correspond to the terms
        a[j] and a[j'] respectively then d[i] = j' - j.
    * Let S2(b) be the sum of (d[i] - 1)^2.
    * Define S(b) = S1(b) - k x S2(b).

What is the maximum value of 'S' obtained over all non-empty subsequences of a?
"""

import sys

# Brute force solution checks every subsequence: O(n^2)
# Score: 0.00 - Terminated due to time out
def modifiedSubsequenceSum_brute(n, k, A):
    totalSum = 0
    S = None
    for i in xrange(n):
        totalSum += A[i]
        S = max(totalSum, A[i], S)
        for j in xrange(i+1, n):
            newSum = totalSum + A[j]
            S2 = pow((j-i-1), 2)
            newS = newSum - (k*S2)
            S = max(S, newS)
    return S

# Submitted: 4.48/64 - Wrong Answer
def modifiedSubsequenceSum(n, k, A):
    S_prev = A[0]
    i = 0
    S_sum = A[0]
    totalSum = A[0]
    for j in xrange(1, n):
        curSum = S_sum + A[j]
        totalSum += A[j]
        S_cur = curSum - (k*(pow((j-i-1), 2)))
        if A[j] > S_cur and A[j] > S_prev:
            S_prev = A[j]
            S_sum = A[j]
            i = j
        elif S_cur > S_prev:
            i = j
            S_sum += A[j]
            S_prev = S_cur
    return max(S_prev, totalSum)

if __name__ == "__main__":
    n, k = raw_input().strip().split(' ')
    n, k = [int(n), int(k)]
    A = map(long, raw_input().strip().split(' '))
    result = modifiedSubsequenceSum(n, k, A)
    print result
