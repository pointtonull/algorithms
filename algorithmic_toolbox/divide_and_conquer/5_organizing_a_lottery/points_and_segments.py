# Uses python3

import random
import sys


START, POINT, END = -1, 0, 1


def fast_count_segments(segments, points):
    universe = [(point, POINT) for point in points]
    for start, end in segments:
        universe.append((start, START))
        universe.append((end, END))
    universe.sort()

    counts = {point: 0 for point in points}
    active_segments = 0
    for pos, label in universe:
        if label is POINT:
            counts[pos] = active_segments
        else:
            active_segments -= label
    return [counts[point] for point in points]


def naive_count_segments(segments, points):
    cnt = [0] * len(points)
    for i, point in enumerate(points):
        for starts, ends in segments:
            if starts <= point <= ends:
                cnt[i] += 1
    return cnt


def stdin():
    if "tests" in sys.argv:
        tests()
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    m = data[1]
    starts = data[2:2 * n + 2:2]
    ends   = data[3:2 * n + 2:2]
    segments = list(zip(starts, ends))
    points = data[2 * n + 2:]
    cnt = fast_count_segments(segments, points)
    for x in cnt:
        print(x, end=' ')


def test(case, expected):
    print(".", end="", file=sys.stderr)
    print("  %s" % str(case), file=sys.stderr)
    obtained = fast_count_segments(*case)
    if expected != obtained:
        raise ValueError("for case: %s, result: %s was expected, got: %s" % (case,
            expected, obtained))


def tests():
    cases = (
        (
            ([(0, 5), (7, 10)], (1, 6, 11)),
            [1, 0, 0]
        ),
        (
            ([(-10, 10)], (-100, 100, 0)),
            [0, 0, 1]
        ),
        (
            ([(0, 5), (-3, 2), (7, 10)], (1, 6)),
            [2, 0]
        ),
    )
    for case, result in cases:
        test(case, result)
    stress_tests()


def stress_tests():
    random.seed(0)
    while True:
        lenght = random.randrange(1, 10)
        segments = [(random.randrange(10), random.randrange(10))
                    for _ in range(lenght)]
        segments = [(left, left + lenght)
                    for left, lenght in segments]
        lenght = random.randrange(1, 10)
        points = [random.randrange(10)
                  for _ in range(lenght)]
        expected = naive_count_segments(segments, points)
        test((segments, points), expected)

if __name__ == '__main__':
    stdin()
