# Uses python3

from itertools import chain, combinations
from collections import defaultdict
import random
import sys


def optimal_weight(capacity, weights):
    cum = [[0 for x in range(len(weights) + 1) ]
           for x in range(capacity + 1)]
    for i in range(len(weights)): 
        for w in range(capacity + 1): 
            if i == 0 or w == 0: 
                cum[i][capacity] = 0
            elif wt[i-1] <= w: 
                cum[i][capacity] = max(val[i - 1] + cum[i - 1][w-wt[i - 1]],
                                cum[i - 1][w])
            else: 
                cum[i][w] = cum[i-1][w]
    return cum[capacity][W] 


def optimal_weight_naive(capacity, weights):
    maximun = 0
    for amount in range(1, capacity + 1):
        for picked in combinations(weights, amount):
            weight = sum(picked)
            if weight <= capacity and weight > maximun:
                show("%s: %d" % (picked, weight))
                maximun = weight
    return maximun


def stdin():
    if "tests" in sys.argv:
        return tests()

    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))


def show(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


def test(function, case, expected):
    show("%s%s" % (getattr(function, "__name__", "Case: "), case))
    show("    => %s" % expected, end="")
    obtained = function(*case)
    if expected != obtained:
        show(" [FAILED]\n")
        raise AssertionError(("\n\nFor case: %s,\n"
                              "%s was expected,\n"
                              "%s was obtained.") % (case, expected, obtained))
    else:
        show(" [OK]")


def stress_cases():
    """
    Returns Infinite(TM) (Case, Expected) pairs.
    """
    random.seed(0)
    while True:
        capacity = random.randrange(1, 10)
        bars = capacity + random.randrange(1, 4)
        weights = [random.randrange(10) for _ in range(bars)]
        expected = optimal_weight_naive(capacity, weights)
        yield ((capacity, weights), expected)


def tests():
    cases = (
            ((10, [1, 4, 8]),
             9), # 1 + 8
            )
    for case, expected in chain(cases, stress_cases()):
        test(optimal_weight, case, expected)


if __name__ == '__main__':
    stdin()
