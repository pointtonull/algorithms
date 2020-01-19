# Uses python3

from collections import defaultdict
from itertools import chain
import random
import sys

def get_majority_element(array, left=0, right=None):
    return get_majority_element_naive(array)


def get_majority_element_naive(sequence):
    n = len(sequence)
    votes = defaultdict(int)
    for vote in sequence:
        votes[vote] += 1
        if votes[vote] > (n / 2):
            return vote
    else:
        return -1


def stdin():
    if "tests" in sys.argv:
        return tests()

    input = sys.stdin.read()
    _, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)


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
        lenght = random.randrange(1, 10)
        array = [random.randrange(10) for _ in range(lenght)]
        expected = get_majority_element_naive(array)
        yield ((array,), expected)


def tests():
    cases = (
            ((list(range(5)),), -1),
            ((list(range(5)),), -1),
            (([1, 1, 2, 2, 3],), -1),
            (([1, 1, 2, 2, 1],), 1),
            (([1, 1, 2, 2, 1, 0],), -1),
            )
    for case, expected in chain(cases, stress_cases()):
        test(get_majority_element, case, expected)


if __name__ == '__main__':
    stdin()
