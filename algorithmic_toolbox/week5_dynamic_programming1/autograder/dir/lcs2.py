# Uses python3

from itertools import chain
from textwrap import indent
import random
import sys


def lcs2(left, right):
    show(left, right)
    pos_dist = {(row, 0): row for row in range(len(left) + 1)}
    pos_dist.update({(0, col): col for col in range(len(right) + 1)})
    show(pos_dist)

    # Operations:
    #   - +(1, 0) Insertion
    #   - +(0, 1) Deletion
    #   - +(1, 1) Substitution
    for row in range(1, len(left) + 1):
        for col in range(1, len(right) + 1):
            is_different = int(left[row - 1] != right[col - 1])
            pos_dist[(row, col)] = min(
                                       pos_dist[(row, col - 1)] + 1,
                                       pos_dist[(row - 1, col)] + 1,
                                       pos_dist[(row - 1, col - 1)] + is_different,
                                      )
    return pos_dist[(row, col)]


def lcs2_naive(a, b):
    return min(len(a), len(b))


def stdin():
    if "tests" in sys.argv:
        return tests()

    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))


def show(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


def test(function, case, expected):
    show("%s%s" % (getattr(function, "__name__", "Case: "), case))
    show("    => %s" % expected, end="")
    obtained = function(*case)
    if expected != obtained:
        show(" [FAILED]\n")
        message = indent(("\nFor case: %s,\n"
                          "%s was expected,\n"
                          "%s was obtained.") % (case, expected, obtained),
                         " " * 4)
        raise AssertionError(message)
    else:
        show(" [OK]")


def stress_cases():
    """
    Returns Infinite(TM) (Case, Expected) pairs.
    """
    random.seed(0)
    while True:
        lenght_left = random.randrange(1, 20)
        lenght_right = lenght_left + random.randrange(20)
        left  = [random.randrange(100) for _ in range(lenght_left)]
        right = [random.randrange(100) for _ in range(lenght_right)]
        expected = lcs2_naive(left, right)
        yield ((left, right), expected)


def tests():
    cases = (
            (([2, 7, 5], [2, 5]),           2),
            (([7], [1, 2, 3, 4]),           0),
            (([2, 7, 8, 3], [5, 2, 8, 7]),  2),
            )
    for case, expected in chain(cases, stress_cases()):
        test(lcs2, case, expected)


if __name__ == '__main__':
    stdin()
