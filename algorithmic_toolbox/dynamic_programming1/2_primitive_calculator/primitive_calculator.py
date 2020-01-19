# Uses python3

from itertools import chain
from itertools import permutations
from math import ceil
from textwrap import indent
import random
import sys

OPERATIONS = [lambda n: n + 1, lambda n: n * 2, lambda n: n * 3]


def optimal_sequence(number):
    array = [(pos, None) for pos in range(number + 1)]
    hist = (1, )
    array[1] = (0, hist)
    pos = 0
    for pos in range(2, number + 1):
        answers = [(array[pos - 1][0] + 1, pos - 1)]
        if not (pos % 3):
            answers.append((array[pos // 3][0] + 1, pos // 3))
        if not (pos % 2):
            answers.append((array[pos // 2][0] + 1, pos // 2))
        cost, prev_pos = min(answers)
        hist = array[prev_pos][1] + (pos,)
        array[pos] = (cost, hist)
    return hist


def optimal_sequence_naive(number):
    minimun_posible = ceil(number / 3)
    for needed in range(minimun_posible, number + 1):
        for permutation in permutations(OPERATIONS, needed):
            attempt = 1
            for operation in permutation:
                attempt = operation(attempt)
            if number == attempt:
                return needed
    else:
        raise ValueError("Could not find combination of %s for %d." % (
            OPERATIONS, number))


def stdin():
    if "tests" in sys.argv:
        return tests()

    input = sys.stdin.read()
    n = int(input)
    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')


def show(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


def test(function, case, expected):
    show("%s%s" % (getattr(function, "__name__", "Case: "), case))
    show("    => %s" % expected, end="")
    obtained = list(function(*case))
    if len(expected) != len(obtained):
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
        number = random.randrange(1, 10e6)
        expected = list(optimal_sequence_naive(number))
        yield ((number,), expected)


def tests():
    cases = (
            ((1,), [1]),
            ((5,), [1, 2, 4, 5]),
            ((96234,), [1, 3, 9, 10, 11, 22, 66, 198, 594, 1782, 5346, 16038,
                        16039, 32078, 96234]),
            )
    for case, expected in chain(cases, stress_cases()):
        test(optimal_sequence, case, expected)


if __name__ == '__main__':
    stdin()
