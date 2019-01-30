# Uses python3

import random
import sys


def fibonacci_partial_sum_naive(from_, to):
    total = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            total += current

        current, next = next, current + next

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


def fibonacci_partial_sum_optimized(pos_from, pos_to):
    total = 0

    period = pisano(10)
    fib_mod = [fib % 10 for fib in fib_seq(period - 2)]

    total =  sum(fib_mod[pos_from % period:])
    total += sum(fib_mod) * (pos_to - pos_from // 10)
    total += sum(fib_mod[:pos_to % period + 1])

    return total % 10


def stress():
    random.seed(0)
    while True:
        pos_from = random.randrange(1, 200)
        pos_to = pos_from + random.randrange(1, 20)
        naive = fibonacci_partial_sum_naive(pos_from, pos_to)
        optimized = fibonacci_partial_sum_optimized(pos_from, pos_to)
        if naive == optimized:
            print("%20s: %s" % ("{pos_from}-{pos_to}".format(**locals()),
                                "{naive} == {optimized}".format(**locals())))
        else:
            raise ValueError("Not the right answser for {pos_from}-{pos_to}: ".format(
                **locals()) + "{naive} != {optimized}".format(**locals()))



if __name__ == '__main__':
#     stress()
    input = sys.stdin.read();
    from_, to = map(int, input.split())
    print(fibonacci_partial_sum_optimized(from_, to))
