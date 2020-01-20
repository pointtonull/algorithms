from copy import deepcopy as copy

from pytest import fixture

from src.find_the_gap import find_the_gap

"""
FIND THE GAP

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
give 3.

You can modify the input array in-place.
"""

CASES = [
    {
        "numbers": [3, 4, -1, 1],
        "answer": 2,
    },
    {
        "numbers": [1, 2, 0],
        "answer": 3,
    },
    {
        "numbers": [1, 2, 0, 3],
        "answer": 4,
    },
    {
        "numbers": [1, 2, 0, 4],
        "answer": 3,
    },
    {
        "numbers": [4, 3, 2, 1],
        "answer": 5,
    },
]



@fixture(params=CASES)
def case(request):
    return copy(request.param)  # modifies in place


def test__find_the_gap__signature(case):
    numbers = case["numbers"]

    result = find_the_gap(numbers)
    assert isinstance(result, int)


def test__find_the_gap__examples(case):
    numbers = case["numbers"]
    answer = case["answer"]

    result = find_the_gap(numbers)
    assert answer == result
