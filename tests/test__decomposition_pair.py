from pytest import fixture

from utils import deep_diff

from src.decomposition_pair import decomposition_pair

"""
Decomposition pair

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""

CASES = [
    {
        "numbers": [10, 15, 3, 7],
        "total": 17,
        "answer": True, # 10 + 7 -> 17
    },
    {
        "numbers": [10, 15, 3, 7],
        "total": 19,
        "answer": False,
    },
]



@fixture(params=CASES)
def case(request):
    return request.param


def test__decomposition_pair__signature(case):
    numbers = case["numbers"]
    total = case["total"]

    result = decomposition_pair(numbers, total)
    assert isinstance(result, bool)


def test__decomposition_pair__examples(case):
    numbers = case["numbers"]
    total = case["total"]
    answer = case["answer"]

    result = decomposition_pair(numbers, total)
    assert answer == result

