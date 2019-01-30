# Uses python3

from copy import copy
from itertools import chain
import random
import sys


def partition3(array, left, right):
    pivot = array[left]
    smallers = []
    equals = [pivot]
    largers = []
    for pos in range(left + 1, right + 1):
        if array[pos] < pivot:
            smallers.append(array[pos])
        elif array[pos] == pivot:
            equals.append(array[pos])
        else:
            largers.append(array[pos])
    show("  %s + %s + %s" % (smallers, equals, largers))
    array[left: right + 1] = smallers + equals + largers
    return len(smallers), len(smallers) + len(equals) - 1


def randomized_quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    smallers = []
    equals = []
    largers = []
    for element in array:
        if element < pivot:
            smallers.append(element)
        elif element == pivot:
            equals.append(element)
        else:
            largers.append(element)

    sleft = randomized_quick_sort(smallers)
    sright = randomized_quick_sort(largers)
    return sleft + equals + sright


def stdin():
    if "tests" in sys.argv:
        return tests()

    input = sys.stdin.read()
    _, *array = list(map(int, input.split()))
    array = randomized_quick_sort(array)
    for x in array:
        print(x, end=' ')


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
        expected = sorted(array)
        yield ((array,), expected)


def tests():
    cases = (
            (([5, 4, 3, 2, 1, 0],),
             [0, 1, 2, 3, 4, 5]),
            (([0, 1, 2, 3, 4, 5],),
             [0, 1, 2, 3, 4, 5]),
            )
    for case, expected in chain(cases, stress_cases()):
        test(randomized_quick_sort, case, expected)


if __name__ == '__main__':
    stdin()
