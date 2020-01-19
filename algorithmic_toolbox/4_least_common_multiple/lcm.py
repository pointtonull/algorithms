# Uses python3

from collections import defaultdict
from functools import reduce
import random
import sys


def lcm_naive(a, b):
    for l in range(1, a*b + 1):
        if l % a == 0 and l % b == 0:
            return l
    return a*b



# def prime_divisors(n):
#     d = defaultdict(int)
#     c = 2
#     while n != 1:
#         if not n % c:
#             n /= c
#             d[c] += 1
#         else:
#             c += 1
#     return d


# def lcm_optimized(a, b):
#     a_prime_divisors = prime_divisors(a)
#     b_prime_divisors = prime_divisors(b)
#     common_divisors = {key: max(a_prime_divisors[key], b_prime_divisors[key])
#                        for key in a_prime_divisors.keys()|b_prime_divisors.keys()}
#     lcm = reduce(lambda a, b: a * b,
#                  (k ** v  for k, v in common_divisors.items()),
#                  1)
#     return lcm


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm_optimized(a, b):
    if a == 0 and b == 0:
        lcm = 0
    else:
        lcm = a * b // gcd(a, b)
    return lcm


def stress():
    random.seed(0)
    while True:
        a, b = [random.randrange(1, 20000) for i in range(2)]
        naive = lcm_naive(a, b)
        optimized = lcm_optimized(a, b)
        if naive == optimized:
            print("%20s: %s" % ("{a}, {b}".format(**locals()),
                                "{naive} == {optimized}".format(**locals())))
        else:
            raise ValueError("Not the right answser for ({a}, {b}): ".format(**locals()) +
                             "{naive} != {optimized}".format(**locals()))



if __name__ == '__main__':
#     stress()
    input = sys.stdin.read()
    a, b = map(int, input.split())
#     print(lcm_naive(a, b))
    print(lcm_optimized(a, b))

