# Uses python3

import random
import sys
import logging

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    total    = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        total += current

    return total % 10


def fib_seq(limit=None):
    a = 0
    yield a
    b = 1
    yield b
    if limit is None:
        while True:
            a, b = b, a + b
            yield b
    else:
        for _ in range(limit):
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


def fibonacci_sum_optimized(n):
    if n <= 1:
        return n

    period = pisano(10)
    fib_mod = [fib % 10 for fib in fib_seq(period - 2)]
#     print(period)
#     print(len(fib_mod), fib_mod)
    total = sum(fib_mod) * (n // 10) + sum(fib_mod[:n % period + 1])

    return total % 10


def stress():
    random.seed(0)
    while True:
        a = random.randrange(1, 20)
        naive = fibonacci_sum_naive(a)
        optimized = fibonacci_sum_optimized(a)
        if naive == optimized:
            print("%20s: %s" % ("{a}".format(**locals()),
                                "{naive} == {optimized}".format(**locals())))
        else:
            raise ValueError("Not the right answser for {a}: ".format(**locals()) +
                             "{naive} != {optimized}".format(**locals()))


if __name__ == '__main__':
#     stress()
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_optimized(n))
