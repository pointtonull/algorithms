from pytest import fixture

from src.no_odd_digits import has_no_odd_digits

"""
NO_ODD_DIGITS

Write a function in a language of your choice which, when passed a positive
integer returns true if the decimal representation of that integer contains no
odd digits and otherwise returns false.
"""

CASES = [
    {
        "input1": 0,
        "answer": True,
    },
    {
        "input1": 1,
        "answer": False,
    },
    {
        "input1": 2,
        "answer": True,
    },
    {
        "input1": 3,
        "answer": False,
    },
    {
        "input1": 4,
        "answer": True,
    },
    {
        "input1": 143,
        "answer": False,
    },
    {
        "input1": 144,
        "answer": False,
    },
    {
        "input1": 244,
        "answer": True,
    },
]



@fixture(params=CASES)
def case(request):
    return request.param


def test__has_no_odd_digits__examples(case):
    input1 = case["input1"]
    answer = case["answer"]

    result = has_no_odd_digits(input1)
    assert answer == result

