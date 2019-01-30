# Uses python3

import sys
import random

def gcd_naive(a, b):
    current_gcd = 1
    for d in range(2, min(a, b) + 1):
        if a % d == 0 and b % d == 0:
            if d > current_gcd:
                current_gcd = d

    return current_gcd


def gcd_optimized(a, b):
    if b == 0:
        return a
    return gcd_optimized(b, a % b)


def stress():
    random.seed(0)
    while True:
        a, b = [random.randrange(1, 200000) for i in range(2)]
        naive = gcd_naive(a, b)
        optimized = gcd_optimized(a, b)
        if naive == optimized:
            print("%20s: %s" % ("{a}, {b}".format(**locals()),
                                "{naive} == {optimized}".format(**locals())))
        else:
            raise ValueError("Not the right answser for ({a}, {b}): ".format(**locals()) +
                             "{naive} != {optimized}".format(**locals()))



if __name__ == "__main__":
#     stress()
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_optimized(a, b))
