# https://www.hackerrank.com/challenges/symmetric-difference/problem

M = int(raw_input().strip())
m_set = set(map(int, raw_input().strip().split()))
N = int(raw_input().strip())
n_set = set(map(int, raw_input().strip().split()))

print '\n'.join(map(str, sorted(list(m_set.difference(n_set).union(n_set.difference(m_set))))))
