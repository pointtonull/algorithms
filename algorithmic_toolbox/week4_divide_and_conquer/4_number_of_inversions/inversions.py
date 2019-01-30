# Uses python3

import sys
import random


def count_inversions_sub(array):
    if len(array) <= 1:
        return array, 0

    center = len(array) // 2
    inversions = 0

    left_array = array[:center]
    left_array, new_inversions = count_inversions_sub(left_array)
    inversions += new_inversions

    right_array = array[center:]
    right_array, new_inversions = count_inversions_sub(right_array)
    inversions += new_inversions

    sorted_array = []
    while left_array and right_array:


        if left_array[0] <= right_array[0]:
            sorted_array.append(left_array.pop(0))
        else:
            sorted_array.append(right_array.pop(0))
            inversions += len(left_array)

    sorted_array += left_array
    sorted_array += right_array

    return sorted_array, inversions


def count_inversions(array):
    array, count = count_inversions_sub(array)
    print("   %s" % array, file=sys.stderr)
    return count


def count_inversions_naive(array):
    inversions = 0
    for pos, left in enumerate(array):
        inversions += sum(left > right for right in array[pos:])
    return inversions


def stdin():
    if "tests" in sys.argv:
        tests()
    input = sys.stdin.read()
    n, *array = list(map(int, input.split()))
    print(count_inversions(array))


def test(case, expected):
    print(".", end="", file=sys.stderr)
    print("  %s" % case, file=sys.stderr)
    obtained = count_inversions(case)
    if expected != obtained:
        raise ValueError("for case: %s, result: %s was expected, got: %s" % (case,
            expected, obtained))


def tests():
    cases = (
            ([2, 3, 9, 2, 9], 2),
            ([5, 4, 3, 2, 1], 10),
            ([9, 8, 7, 3, 2, 1], 15),
            )
    for case, result in cases:
        test(case, result)
    stress_tests()


def stress_tests():
    random.seed(0)
    while True:
        lenght = random.randrange(1, 10)
        array = [random.randrange(10) for _ in range(lenght)]
        expected = count_inversions_naive(array)
        test(array, expected)

if __name__ == '__main__':
    stdin()
