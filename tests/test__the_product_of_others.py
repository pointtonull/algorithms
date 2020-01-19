from pytest import fixture

from utils import deep_diff

from src.the_product_of_others import the_product_of_others

"""
THE PRODUCT OF OTHERS

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i 
of the new array is the product of all the numbers in the original array except
the one at i.


Follow-up: what if you can't use division?
"""

CASES = [
    {
        "numbers": [1, 2, 3, 4, 5],
        "answer": [120, 60, 40, 30, 24],
    },
    {
        "numbers": [3, 2, 1],
        "answer": [2, 3, 6],
    },
    {
        "numbers": [3, 0, 1],
        "answer": [0, 3, 0],
    },
]



@fixture(params=CASES)
def case(request):
    return request.param


def test__the_product_of_others__signature(case):
    numbers = case["numbers"]

    result = the_product_of_others(numbers)
    assert isinstance(result, list)


def test__the_product_of_others__examples(case):
    numbers = case["numbers"]
    answer = case["answer"]

    result = the_product_of_others(numbers)
    assert answer == result

