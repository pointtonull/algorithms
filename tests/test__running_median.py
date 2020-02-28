from random import Random
from typing import Sequence, Generator

from pytest import fixture

from src.running_median import running_median, running_median_naive

random = Random(0)

"""
RUNNING MEDIAN

This problem was asked by Microsoft.
Difficulty: Easy

Compute the running median of a sequence of numbers. That is, given a stream of
numbers, print out the median of the list so far on each new element.

Recall that the median of an even-numbered list is the average of the two middle
numbers.

"""

CASES = [
    {
        "sequence":  [2,  1,    5,  7,    2,  0,  5],
        "answer":    [2,  1.5,  2,  3.5,  2,  2,  2]
    },
]



@fixture(params=CASES)
def case(request):
    return request.param


@fixture(params=range(1, 100))
def case_stress(request):
    return [random.randrange(10) for _ in range(request.param)]


def test__running_median__signature(case):
    sequence = case["sequence"]

    result = running_median(sequence)
    assert isinstance(result, (Sequence, Generator))


def test__running_median__examples(case):
    sequence = case["sequence"]
    answer = case["answer"]

    result = running_median(sequence)
    assert answer == list(result)


def test__running_median_naive__signature(case):
    sequence = case["sequence"]

    result = running_median_naive(sequence)
    assert isinstance(result, (Sequence, Generator))


def test__running_median_naive__examples(case):
    sequence = case["sequence"]
    answer = case["answer"]

    result = running_median_naive(sequence)
    assert answer == list(result)


def test__running_median__stress(case_stress):
    sequence = case_stress

    answer = running_median_naive(sequence)
    result = running_median(sequence)
    assert list(answer) == list(result)
