#Uses python3

from functools import cmp_to_key
from itertools import permutations
import random
import sys


def cmp_salary(a, b):
    return int(a + b) - int(b + a)


def largest_number(numbers):
    numbers = sorted(numbers, key=cmp_to_key(cmp_salary), reverse=True)
    return "".join(numbers)


def largest_number_naive(numbers):
    largest = 0
    for order in permutations(numbers, len(numbers)):
        number = int("".join(order))
        largest = max(largest, number)
    return str(largest)


def stdin():
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))


def equal_enough(left, right):
    return abs(left - right) < 0.0001


def test(case, expected):
    print(".", end="", file=sys.stderr)
    obtained = largest_number(case)
    if int(expected) != int(obtained):
        raise ValueError("for case: %s, result: %s was expected, got: %s" % (case,
            expected, obtained))


def tests():
    cases = {
            ("21", "2"): "221",
            ("9", "4", "6", "1", "9"): "99641",
            ("23", "39", "92"): "923923",
            ("9", "8", "97", "96", "123"): "997968123",
            }
    for case, result in cases.items():
        test(case, result)

def stress_test():
    random.seed(0)
    while True:
        lenght = random.randrange(1, 6)
        numbers = [str(random.randrange(100)) for _ in range(lenght)]
        expected = largest_number_naive(numbers)
        test(numbers, expected)

if __name__ == '__main__':
#     tests()
#     stress_test()
    stdin()
