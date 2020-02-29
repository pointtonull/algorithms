from pytest import fixture

from src.largest_adjacent_sum import largest_adjacent_sum

"""
LARGEST NON-ADJACENT SUM

This problem was asked by Airbnb.

Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative. 

Follow-up: Can you do this in O(N) time and constant space?
"""

CASES = [
    {
        "numbers": [],
        "answer": 0
    },
    {
        "numbers": [4],
        "answer": 4
    },
    {
        "numbers": [2, 4, 6, 2, 5],
        "answer": 13  # 2 + 6 + 5
    },
    {
        "numbers": [5, 1, 1, 5],
        "answer": 10  # 5 + 5
    },
]



@fixture(params=CASES)
def case(request):
    return request.param


def test__largest_adjacent_sum__signature(case):
    numbers = case["numbers"]

    result = largest_adjacent_sum(numbers)
    assert isinstance(result, int)


def test__largest_adjacent_sum__examples(case):
    numbers = case["numbers"]
    answer = case["answer"]

    result = largest_adjacent_sum(numbers)
    assert answer == result

