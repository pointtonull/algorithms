# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    value = 0.
    items = sorted(((value/weight, value, weight)
                   for value, weight in zip(values, weights)), reverse=True)

    for density, item_value, item_weight in items:
        portion = min(item_weight, capacity)
        portion_value = density * portion
        capacity -= portion
        value += portion_value

    return float(value)


def stdin():
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))


def equal_enough(left, right):
    return abs(left - right) < 0.0001


def test(case, expected):
    obtained = get_optimal_value(*case)
    if not equal_enough(expected, obtained):
        raise ValueError("for case %s, result %s was expected, got %s" % (case,
            expected, obtained))


def tests():
    cases = {
                (50, (20, 50, 30), (60, 100, 120)): 180.,
                (10, (30,), (500,)): 500/3.
            }
    for case, result in cases.items():
        test(case, result)


if __name__ == "__main__":
#     tests()
    stdin()
