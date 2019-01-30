#Uses python3

from itertools import combinations
import math
import random
import sys



def distance(p_from, p_to):
    x_from, y_from = p_from
    x_to, y_to = p_to
    return ((x_from - x_to) ** 2 + (y_from - y_to) ** 2) ** .5


def minimum_distance(points):
    x_axis = sorted(points)
    y_axis = sorted(points, key=lambda point: point[::-1])
    point1, point2, min_distance = split(x_axis, y_axis)
    return min_distance


def split(x_axis, y_axis):
    if len(x_axis) <= 3:
        return minimum_distance_naive(x_axis)

    pivot = len(x_axis) // 2
    left_x = x_axis[:pivot]
    right_x = x_axis[pivot:]

    spliter = x_axis[pivot][0]
    left_y = []
    right_y = []
    for x, y in y_axis:
        if x <= spliter:
            left_y.append((x, y))
        else:
            right_y.append((x, y))

    point1_x, point2_x, min_distance_x = split(left_x, left_x)
    point1_y, point2_y, min_distance_y = split(right_x, right_y)

    if min_distance_x < min_distance_y:
        min_distance = min_distance_x
        point1, point2 = point1_x, point2_x
    else:
        min_distance = min_distance_y
        point1, point2 = point1_y, point2_y

    result = closest_pair_border(x_axis, y_axis, min_distance, (point1, point2))
    point1_border, point2_border, min_distance_border = result

    if min_distance <= min_distance_border:
        return point1, point2, min_distance
    else:
        return point1_border, point2_border, min_distance_border


def closest_pair_border(x_axis, y_axis, margin, current_pair):

    pivot = len(y_axis) // 2
    border, y_middle = x_axis[pivot]

    filtered_y = [(x, y)
                  for x, y in y_axis
                  if border - margin <= x <= border + margin]

    for i in range(len(filtered_y) - 1):
        for j in range(i + 1, min(i + 7, len(filtered_y))):
            point1, point2 = filtered_y[i], filtered_y[j]
            this_distance = distance(point1, point2)
            if this_distance < margin:
                current_pair = point1, point2
                margin = this_distance

    return current_pair[0], current_pair[1], margin


def minimum_distance_naive(points):
    return min(((point1, point2, distance(point1, point2))
                for point1, point2 in combinations(points, 2)),
               key=lambda item:item[-1])


def show(*args, **kwargs):
    print(*args, **kwargs, file=sys.stderr)


def stdin():
    if "tests" in sys.argv:
        return tests()

    input = sys.stdin.read()
    data = list(map(int, input.split()))
    x = data[1::2]
    y = data[2::2]
    points = list(zip(x, y))
    print("{0:.9f}".format(minimum_distance(points)))


def equal_enough(left, right):
    try:
        return abs(left - right) < 0.0001
    except:
        return False


def test(case, expected):
    show(".", end="")
    show("  %s" % str(case))
    obtained = minimum_distance(case)
    if not equal_enough(expected, obtained):
        raise ValueError(("for case: %s, result:\n"
                          "%s was expected,\n"
                          "%s was obtained") % (case, expected, obtained))


def tests():
    cases = (
        (
            ((0, 0), (3, 4)),
            5.0 # only one pair
        ),
        (
            ((7, 7), (1, 100), (4, 8), (7, 7)),
            0.0 # twice the same point
        ),
        (
            ((4, 4), (-2, -2), (-3, -4), (-1, 3), (2, 3), (-4, 0), (1, 1),
            (-1, -1), (3, -1), (-4, 2), (-2, 4)), # sqrt(2)
            1.414213
        ),
    )
    for case, result in cases:
        test(case, result)
    stress_tests()


def stress_tests():
    random.seed(0)
    while True:
        lenght = random.randrange(2, 10)
        points = [(random.randrange(10), random.randrange(10))
                  for _ in range(lenght)]
        result = minimum_distance_naive(points)
        show("expected = %s" % str(result))
        expected = result[-1]
        test(points, expected)

if __name__ == '__main__':
    stdin()
#     tests()
