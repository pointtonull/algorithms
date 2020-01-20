from pytest import fixture

from utils import deep_diff

from src.twisted_pair import car, cdr, cons

"""
TWISTED PAIR

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and
last element of that pair. For example, car(cons(3, 4)) returns 3, and 
cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


Implement car and cdr.
"""

CASES = [
    {
        "pair": cons(3, 4),
        "function": car,
        "answer": 3,
    },
    {
        "pair": cons(3, 4),
        "function": cdr,
        "answer": 4,
    },
]



@fixture(params=CASES)
def case(request):
    return request.param


def test__car__signature(case):
    pair = case["pair"]
    function = case["function"]

    result = function(pair)
    assert isinstance(result, int)


def test__car__examples(case):
    pair = case["pair"]
    function = case["function"]
    answer = case["answer"]

    result = function(pair)
    assert answer == result

