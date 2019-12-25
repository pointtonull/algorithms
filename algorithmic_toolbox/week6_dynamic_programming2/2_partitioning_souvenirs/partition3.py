# Uses python3

from itertools import chain, combinations, product
from collections import defaultdict
import random
import sys


def partition3(A):
        n = len(A)
        S = sum(A)

        if S % 3 != 0:
            return 0

        T = [[[None for _ in range(S + 1)] for _ in range(S + 1)] for _ in range(n + 1)]
        for (s1, s2) in product(range(S // 3 + 1), repeat=2):
            if s1 == 0 and s2 == 0:
                T[0][s1][s2] = 1
            else:
                T[0][s1][s2] = 0

        for i in range(1, n + 1):
            for (s1, s2) in product(range(S // 3 + 1), repeat=2):
                T[i][s1][s2] = T[i - 1][s1][s2]
                if s1 >= A[i - 1]:
                    T[i][s1][s2] = max(T[i - 1][s1][s2], T[i - 1][s1 - A[i - 1]][s2])
                if s2 >= A[i - 1]:
                    T[i][s1][s2] = max(T[i - 1][s1][s2], T[i - 1][s1][s2 - A[i - 1]])

        return T[n][S // 3][S // 3]

def partition3_naive(A):
    for c in product(range(3), repeat=len(A)):
        sums = [None] * 3
        for i in range(3):
            sums[i] = sum(A[k] for k in range(len(A)) if c[k] == i)

        if sums[0] == sums[1] and sums[1] == sums[2]:
            return 1

    return 0


def stdin():
    if "tests" in sys.argv:
        return tests()

    input = sys.stdin.read()
    n, *A = list(map(int, input.split()))
    print(partition3(A))


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
