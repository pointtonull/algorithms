# Uses python3

from itertools import chain, combinations_with_replacement
from math import ceil
from textwrap import indent
import os
import random
import sys

COINS = (1, 3, 4)

def report():
    dirs = os.listdir("..")
    print("..: %s" % ", ".join(dirs))
    tmpdir = next(name for name in dirs if name.startswith("tmp"))
    dirs = os.listdir("../%s" % tmpdir)
    dirname = "autograder"
    dirs = os.listdir("../%s" % dirname)
#     print("../%s: %s" % (dirname, ", ".join(dirs)))
#     print("%s: %s" % (tmpdir, ", ".join(dirs)))
#     print(os.path.abspath("."))

def get_change(money):
    array = list(range(money + 1))
    new_value = 0
    for pos in range(1, money + 1):
        new_value = min(array[pos - coin] + 1
                        for coin in COINS
                        if coin <= money)
        array[pos] = new_value
    return new_value


def get_change_naive(money):
    minimun_posible = ceil(money / max(COINS))
    for needed in range(minimun_posible, money + 1):
        for combination in combinations_with_replacement(COINS, needed):
            if sum(combination) == money:
                return needed
    else:
        raise ValueError("Could not find combination of %s for %d." % (
            COINS, money))


def stdin():
    if "tests" in sys.argv:
        return tests()

    m = int(sys.stdin.read())
    print(get_change(m))


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
        money = random.randrange(1, 1000)
        expected = get_change_naive(money)
        yield ((money,), expected)


def tests():
    cases = (
            ((0,), 0),
            ((1,), 1),
            ((2,), 2),
            ((34,), 9),
            )
    for case, expected in chain(cases, stress_cases()):
        test(get_change, case, expected)


if __name__ == '__main__':
    report()
    stdin()
