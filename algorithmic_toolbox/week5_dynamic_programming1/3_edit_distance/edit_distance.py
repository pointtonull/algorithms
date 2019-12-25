# Uses python3

from itertools import chain
from string import ascii_lowercase as UNIVERSE
from textwrap import indent
import random
import sys

try:
    from Levenshtein import distance
except:
    distance = lambda left, right: 0


def edit_distance(left, right):
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


def edit_distance_naive(left, right):
    return distance(left, right)


def stdin():
    if "tests" in sys.argv:
        return tests()

    print(edit_distance(input(), input()))


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
        lenght_left = random.randrange(5, 21)
        lenght_right = lenght_left + random.randrange(5) - 2
        left = "".join(random.sample(UNIVERSE, lenght_left))
        right = "".join(random.sample(UNIVERSE, lenght_right))
        expected = edit_distance_naive(left, right)
        yield ((left, right), expected)


def tests():
    cases = (
            (("ab", "ab"), 0),
            (("short", "ports"), 3),
            (("editing", "distance"), 5),
            )
    for case, expected in chain(cases, stress_cases()):
        test(edit_distance, case, expected)


if __name__ == '__main__':
    stdin()
