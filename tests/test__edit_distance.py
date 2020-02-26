from pytest import fixture

from src.edit_distance import edit_distance

"""
EDIT DISTANCE

This problem was asked by Google.
Difficulty: Easy

The edit distance between two strings refers to the minimum number of character
insertions, deletions, and substitutions required to change one string to the
other.

For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.
"""

CASES = [
    {
        "input1": "kitten",
        "input2": "sitting",
        "answer": 3,
    },
    {
        "input1": "saturday",
        "input2": "sunday",
        "answer": 3,
    },
    {
        "input1": "",
        "input2": "sunday",
        "answer": 6,
    },
    {
        "input1": "saturday",
        "input2": "",
        "answer": 8,
    },
]



@fixture(params=CASES)
def case(request):
    return request.param


def test__edit_distance__signature(case):
    input1 = case["input1"]
    input2 = case["input2"]

    result = edit_distance(input1, input2)
    assert isinstance(result, int)


def test__edit_distance__examples(case):
    input1 = case["input1"]
    input2 = case["input2"]
    answer = case["answer"]

    result = edit_distance(input1, input2)
    assert answer == result

