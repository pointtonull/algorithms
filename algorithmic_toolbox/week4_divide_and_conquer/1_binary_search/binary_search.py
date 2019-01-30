# Uses python3

import sys
import random


def binary_search(array, searched, limits=None):
    if limits:
        left, right = limits
    else:
        left, right = 0, len(array) - 1

    midle = (left + right) // 2
#     print("  %d <%d> %d" % (left, midle, right), file=sys.stderr)
    if searched == array[midle]:
        return midle
    if left >= right:
        return -1
    elif searched < array[midle]:
        return binary_search(array, searched, limits=(left, midle - 1))
    elif searched > array[midle]:
        return binary_search(array, searched, limits=(midle + 1, right))
    # write your code here


def builtin_search(array, searched):
    try:
        return array.index(searched)
    except ValueError:
        return -1


def stdin():
    if "tests" in sys.argv:
        tests()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[n + 1]
    a = data[1 : n + 1]
    for x in data[n + 2:]:
        print(binary_search(a, x), end = ' ')


def equal_enough(left, right):
    return abs(left - right) < 0.0001


def test(case, expected):
    print(".", end="", file=sys.stderr)
    print("  %s, %d" % case, file=sys.stderr)
    obtained = binary_search(*case)
    if expected != obtained:
        raise ValueError("for case: %s, result: %s was expected, got: %s" % (case,
            expected, obtained))


def tests():
    cases = (
            ((sorted(range(5)), 0), 0),
            ((sorted(range(5)), 5), -1),
            )
    for case, result in cases:
        test(case, result)
    stress_tests()


def stress_tests():
    random.seed(0)
    while True:
        lenght = random.randrange(1, 10)
        array = sorted({random.randrange(10) for _ in range(lenght)})
        searched = random.randrange(10)
        expected = builtin_search(array, searched)
        test((array, searched), expected)

if __name__ == '__main__':
    stdin()
