# Uses python3

from itertools import chain, combinations_with_replacement
from math import ceil
from functools import lru_cache
import random
import sys
from textwrap import indent

COINS = (1, 3, 4)


@lru_cache()
def get_change(money):
    if money == 0:
        return 0
    if money in COINS:
        return 1
    else:
        return min(get_change(money - coin)
                   for coin in COINS
                   if coin <= money) + 1


def get_change_naive(money):
    minimun_posible = ceil(money / max(COINS))
    for needed in range(minimun_posible, money + 1):
        for combination in combinations_with_replacement(COINS, needed):
            if sum(combination) == money:
                return needed
    else:
        raise ValueError(f"Could not find combination of {COINS} for {money}.")


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
        money = random.randrange(1, 10)
        expected = get_change_naive(money)
        yield ((money,), expected)


def tests():
    cases = (
            ((2,), 2),
            ((34,), 9),
            )
    for case, expected in chain(cases, stress_cases()):
        test(get_change, case, expected)


if __name__ == '__main__':
    stdin()
