from pytest import fixture

from src.sum_of_even_fibonacci_numbers import (
    sum_of_even_fibonacci_numbers,
    even_fibonacci_numbers,
)

"""
SUM OF EVEN FIBONACCI NUMBERS

Efficient implementation of serie of partial sum of even fibonacci numbers.
"""

CASES_EVEN = [
    {"n": 1, "answer": 2},
    {"n": 2, "answer": 8},
    {"n": 3, "answer": 34},
    {"n": 4, "answer": 144},
    {"n": 5, "answer": 610},
    {"n": 6, "answer": 2584},
]


@fixture(params=CASES_EVEN)
def case(request):
    return request.param


def test__even_fibonacci_numbers__examples(case):
    n = case["n"]
    answer = case["answer"]

    result = even_fibonacci_numbers(n)
    assert answer == result


CASES_SUM_EVEN = [
    {"n": 1, "answer": 2},
    {"n": 2, "answer": 10},
    {"n": 3, "answer": 44},
    {"n": 4, "answer": 188},
    {"n": 5, "answer": 798},
    {"n": 6, "answer": 3382},
    {"n": 7, "answer": 14328},
]


@fixture(params=CASES_SUM_EVEN)
def case_sum(request):
    return request.param


def test__sum_of_even_fibonacci_numbers__examples(case_sum):
    n = case_sum["n"]
    answer = case_sum["answer"]

    result = sum_of_even_fibonacci_numbers(n)
    assert answer == result
