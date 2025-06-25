from pytest import fixture

from src.find_repeated_in_sorted_arrays import find_repeated_in_sorted_arrays

"""
REPEATED IN SORTED ARRAYS

Write a function in a language of your choice which, when passed two sorted
arrays of integers returns an array of any numbers which appear in both. No
value should appear in the returned array more than once.
"""

CASES = [

    {
        "input1": [0, 1, 2, 3, 4, 5, 6, 7],
        "input2": [8, 9, 10, 11, 12, 13, 14],
        "answer": [],
    },
    {
        "input1": [0, 1, 2, 3, 4, 5, 6, 7],
        "input2": [0, 1, 2, 3, 4, 5, 6, 7],
        "answer": [0, 1, 2, 3, 4, 5, 6, 7],
    },
    {
        "input1": [0, 1, 2, 3, 4, 5, 6, 7],
        "input2": [5, 6, 7, 8, 9, 10, 11],
        "answer": [5, 6, 7],
    },
    {
        "input1": [0, 1, 1, 2, 3, 4, 5, 6, 7],
        "input2": [8, 9, 10, 11, 12, 13, 14],
        "answer": [],
    },
    {
        "input1": [0, 1, 1, 2, 3, 4, 5, 6, 7],
        "input2": [0, 1, 1, 2, 3, 4, 5, 6, 7],
        "answer": [0, 1, 2, 3, 4, 5, 6, 7],
    },
    {
        "input1": [0, 1, 2, 3, 4, 5, 6, 7],
        "input2": [5, 6, 7, 8, 9, 10, 11],
        "answer": [5, 6, 7],
    },
]



@fixture(params=CASES)
def case(request):
    return request.param


def test__find_repeated_in_sorted_arrays__examples(case):
    input1 = case["input1"]
    input2 = case["input2"]
    answer = case["answer"]

    result = find_repeated_in_sorted_arrays(input1, input2)
    assert answer == result

