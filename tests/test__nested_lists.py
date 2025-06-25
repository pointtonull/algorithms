from pytest import fixture

from src.nested_lists import nested_lists

"""
NESTED_LISTS

Write a function which is passed an integer, n, and returns a list of n lists such that
   f(0) returns []
   f(1) returns [[1]]
   f(2) returns [[1], [1,2]]
   f(3) returns [[1], [1,2], [1,2,3]]
   etc.
"""

CASES = [
    {
        "n": 0,
        "answer": [],
    },
    {
        "n": 1,
        "answer": [[1]],
    },
    {
        "n": 2,
        "answer": [[1], [1, 2]],
    },
    {
        "n": 3,
        "answer": [[1], [1, 2], [1, 2, 3]],
    },
]


@fixture(params=CASES)
def case(request):
    return request.param


def test__nested_lists__examples(case):
    n = case["n"]
    answer = case["answer"]

    result = nested_lists(n)
    assert answer == result
