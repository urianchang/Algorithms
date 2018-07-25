# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    w = len("{0:b}".format(number)) # 5 -> 0b101 -> 101 -> 3
    for i in xrange(1, number+1):
      print "{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}".format(i, width=w)

print_formatted(int(raw_input().strip()))
