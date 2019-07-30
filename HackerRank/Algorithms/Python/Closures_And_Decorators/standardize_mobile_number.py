# Python 3.7
# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem

def wrapper(f):
    def fun(l: list):
        for i, ns in enumerate(l):
            if len(ns) != 10:
                ns = ns[-10:]
            l[i] = f"+91 {ns[:5]} {ns[5:]}"
        f(l)
    return fun


@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')


if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
