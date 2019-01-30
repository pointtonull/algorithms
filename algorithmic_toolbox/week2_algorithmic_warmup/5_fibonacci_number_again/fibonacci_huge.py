# Uses python3

import random
import sys
from functools import lru_cache

def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m


def fib_seq():
    a = 0
    yield a
    b = 1
    yield b
    while True:
        a, b = b, a + b
        yield b


def fib(n, mod=1):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b % mod, a + b
    return a % mod


def pisano(mod):
    if mod == 1:
        return 1
    fib_mod = (fib % mod for fib in fib_seq())
    _ = next(fib_mod)
    prev = next(fib_mod)
    fib = next(fib_mod)
    for period, fib in enumerate(fib_mod, 2):
        if prev == 0 and fib == 1:
            return period
        else:
            prev = fib


def get_fibonacci_huge_optimized(n, mod):
    if n <= 1:
        return n

    period = pisano(mod)
    pos = n % period
    return fib(pos, mod)


def stress():
    random.seed(0)
    while True:
        a, b = [random.randrange(1, 200000), random.randrange(1, 30)]
        naive = get_fibonacci_huge_naive(a, b)
        optimized = get_fibonacci_huge_optimized(a, b)
        if naive == optimized:
            print("%20s: %s" % ("{a}, {b}".format(**locals()),
                                "{naive} == {optimized}".format(**locals())))
        else:
            raise ValueError("Not the right answser for ({a}, {b}): ".format(**locals()) +
                             "{naive} != {optimized}".format(**locals()))


if __name__ == '__main__':
#     stress()
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_optimized(n, m))
