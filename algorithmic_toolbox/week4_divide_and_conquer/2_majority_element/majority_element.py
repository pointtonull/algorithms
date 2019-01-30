# Uses python3

import sys
from collections import defaultdict
import random

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
        tests()
    input = sys.stdin.read()
    _, *a = list(map(int, input.split()))
    if get_majority_element(a) != -1:
        print(1)
    else:
        print(0)


def show(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


def test(case, expected):
    show("Case: %s, expected: %s" % (case, expected), end="")
    obtained = get_majority_element(case)
    if expected != obtained:
        show(" [FAILED]\n")
        raise AssertionError("\n\nFor case: %s,\n%s was expected,\n%s was obtained." % (case,
            expected, obtained))
    else:
        show(" [OK]")


def tests():
    cases = (
            (list(range(5)), -1),
            (list(range(5)), -1),
            ([1, 1, 2, 2, 3], -1),
            ([1, 1, 2, 2, 1], 1),
            ([1, 1, 2, 2, 1, 0], -1),
            )
    for case, result in cases:
        test(case, result)
    stress_tests()


def stress_tests():
    random.seed(0)
    while True:
        lenght = random.randrange(1, 10)
        array = [random.randrange(10) for _ in range(lenght)]
        expected = get_majority_element_naive(array)
        test(array, expected)

if __name__ == '__main__':
    stdin()
