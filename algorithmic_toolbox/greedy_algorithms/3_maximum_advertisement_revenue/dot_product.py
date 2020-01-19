#Uses python3

import sys

def max_dot_product(estimated_clicks, value_per_click):
    #write your code here
    estimated_clicks = sorted(estimated_clicks, reverse=True)
    value_per_click = sorted(value_per_click, reverse=True)
    total = sum(clicks * value
                for clicks, value in zip(estimated_clicks, value_per_click)
            )
    return total


def stdin():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))


def equal_enough(left, right):
    return abs(left - right) < 0.0001


def test(case, expected):
    obtained = max_dot_product(*case)
    if not equal_enough(expected, obtained):
        raise ValueError("for case %s, result %s was expected, got %s" % (case,
            expected, obtained))


def tests():
    cases = {
                ((23,), (39,)): 897,
                ((1, 3, -5), (-2, 4, 1)): 23.
            }
    for case, result in cases.items():
        test(case, result)

if __name__ == '__main__':
#     tests()
    stdin()
