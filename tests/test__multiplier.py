from pytest import fixture

from src.multiplier import multiplier

"""
MULTIPLIER

Write a function in a language of your choice which, when passed a decimal
digit X, returns the value of X+XX+XXX+XXXX. E.g. if the supplied digit is 3 it
should return 3702 (3+33+333+3333).
"""

CASES = [
    {
        "input1": 1,
        "answer": 1 + 11 + 111 + 1111, # 1234
    },
    {
        "input1": 2,
        "answer": 2 + 22 + 222 + 2222, # 2468
    },
    {
        "input1": 3,
        "answer": 3 + 33 + 333 + 3333, # 3702
    },
    {
        "input1": 4,
        "answer": 4 + 44 + 444 + 4444, # 4936
    },
]


@fixture(params=CASES)
def case(request):
    return request.param


def test__multiplier__examples(case):
    input1 = case["input1"]
    answer = case["answer"]

    result = multiplier(input1)
    assert answer == result
