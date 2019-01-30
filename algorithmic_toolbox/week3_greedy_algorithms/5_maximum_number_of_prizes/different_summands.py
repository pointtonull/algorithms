# Uses python3

from math import floor, sqrt
import sys

def optimal_summands(n):
    kids = floor((sqrt( 1 + 8 * n) - 1) / 2)
    prizes = list(range(1, kids + 1))
    prizes[-1] += n - sum(prizes)
    return prizes


def stdin():
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')


def equal_enough(left, right):
    return abs(left - right) < 0.0001


def test(case, expected):
    print("\nTest:", file=sys.stderr)
    obtained = optimal_summands(case)
    if not equal_enough(expected, len(obtained)):
        raise ValueError("for case: %s, result: %s was expected, got: %s" % (case,
            expected, obtained))



def tests():
    cases = {
            1: 1, 2: 1, 3: 2, 4: 2, 5: 2, 6: 3, 7: 3, 8: 3, 9: 3, 10: 4, 11: 4,
            12: 4, 13: 4, 14: 4, 15: 5, 16: 5, 17: 5, 18: 5, 19: 5, 20: 5, 21:
            6, 22: 6, 23: 6, 24: 6, 25: 6, 26: 6, 27: 6, 28: 7, 29: 7, 30: 7,
            31: 7, 32: 7, 33: 7, 34: 7, 35: 7, 36: 8, 37: 8, 38: 8, 39: 8, 40:
            8, 41: 8, 42: 8, 43: 8, 44: 8, 45: 9, 46: 9, 47: 9, 48: 9, 49: 9,
            50: 9, 51: 9, 52: 9, 53: 9, 54: 9, 55: 10, 56: 10, 57: 10, 58: 10,
            59: 10, 60: 10, 61: 10, 62: 10, 63: 10, 64: 10, 65: 10, 66: 11, 67:
            11, 68: 11, 69: 11, 70: 11, 71: 11, 72: 11, 73: 11, 74: 11, 75: 11,
            76: 11, 77: 11, 78: 12, 79: 12, 80: 12,
            }
    for case, result in cases.items():
        test(case, result)


if __name__ == '__main__':
#     tests()
    stdin()
