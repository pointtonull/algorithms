from pytest import fixture

from src.multiples_generator import multiples_generator

"""
MULTIPLES_GENERATOR

Define a generator which generates the positive integers up to and including a
supplied value which are divisible by another supplied positive integer and use
it to calculate the sum of all positive integers less than 102030 which are
divisible by 3
"""

CASES_GENERATOR = [
    {
        "limit": 1,
        "divisor": 1,
        "answer": [1],
    },
    {
        "limit": 2,
        "divisor": 2,
        "answer": [2],
    },
    {
        "limit": 2,
        "divisor": 1,
        "answer": [1, 2],
    },
    {
        "limit": 2,
        "divisor": 3,
        "answer": [],
    },
    {
        "limit": 20,
        "divisor": 3,
        "answer": [3, 6, 9, 12, 15, 18],
    },
    {
        "limit": 21,
        "divisor": 3,
        "answer": [3, 6, 9, 12, 15, 18, 21],
    },
]


@fixture(params=CASES_GENERATOR)
def case_generator(request):
    return request.param


def test__multiples_generator__examples(case_generator):
    limit = case_generator["limit"]
    divisor = case_generator["divisor"]
    answer = case_generator["answer"]

    result = list(multiples_generator(limit, divisor))
    assert answer == result


CASES_SUM_GENERATOR = [
    {
        "limit": 1,
        "divisor": 1,
        "answer": 1,
    },
    {
        "limit": 2,
        "divisor": 2,
        "answer": 2,
    },
    {
        "limit": 2,
        "divisor": 1,
        "answer": 3,
    },
    {
        "limit": 2,
        "divisor": 3,
        "answer": 0,
    },
    {
        "limit": 20,
        "divisor": 3,
        "answer": sum([3, 6, 9, 12, 15, 18]),
    },
    {
        "limit": 21,
        "divisor": 3,
        "answer": sum([3, 6, 9, 12, 15, 18, 21]),
    },
    {
        "limit": 102030-1,
        "divisor": 3,
        "answer": 1734969135,
    },
]


@fixture(params=CASES_SUM_GENERATOR)
def case_sum_generator(request):
    return request.param


def test__sum_multiples_generator__examples(case_sum_generator):
    limit = case_sum_generator["limit"]
    divisor = case_sum_generator["divisor"]
    answer = case_sum_generator["answer"]

    result = sum(multiples_generator(limit, divisor))
    assert answer == result
