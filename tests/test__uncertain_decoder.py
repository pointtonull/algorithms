from pytest import fixture

from utils import deep_diff

from src.uncertain_decoder import possible_combinations

"""
UNCERTAIN DECODER

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa',
'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not
allowed.
"""

CASES = [
    {"message": "2", "answer": 1},  # "b"
    {"message": "111", "answer": 3},  # "aaa", "ka", "ak"
    {"message": "4", "answer": 1},  # d
]


@fixture(params=CASES)
def case(request):
    return request.param


def test__possible_combinations__signature(case):
    message = case["message"]

    result = possible_combinations(message)
    assert isinstance(result, int)


def test__possible_combinations__examples(case):
    message = case["message"]
    answer = case["answer"]

    result = possible_combinations(message)
    assert not deep_diff(answer, result)
