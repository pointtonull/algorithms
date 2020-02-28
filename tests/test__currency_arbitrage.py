from pytest import fixture

from src.currency_arbitrage import is_inconsistent

"""
CURRENCY ARBITRAGE

This problem was asked by Jane Street.
Difficulty: Hard

Suppose you are given a table of currency exchange rates, represented as a 2D
array. Determine whether there is a possible arbitrage: that is, whether there
is some sequence of trades you can make, starting with some amount A of any
currency, so that you can end up with some amount greater than A of that currency.
There are no transaction costs and you can trade fractional quantities.
"""

CASES = [
    {
        "rates": [],
        "answer": False,
    },
    {
        "rates": [
            [1,    2],
            [1/2,  1]
        ],
        "answer": False,
    },
    {
        "rates":  [
            [1,    2,    3],
            [1/2,  1,    4],
            [1/3,  1/4,  1]
        ],
        "answer": True,
    },
    {
        "rates": [
            [1,    2],
            [1/3,  1]
        ],
        "answer": False,
    },
    {
        "rates":  [
            [1,    2,    3],
            [0.5,  1,    4],
            [1/4,  1/4,  1]
        ],
        "answer": True,
    },
    {
        "rates": [
            [1,    2],
            [2/3,  1]
        ],
        "answer": True,
    },
    {
        "rates":  [
            [1,    2,    3],
            [0.5,  1,    4],
            [1/2,  1/4,  1]
        ],
        "answer": True,
    },
]



@fixture(params=CASES)
def case(request):
    return request.param


def test__is_inconsistent__signature(case):
    rates = case["rates"]

    result = is_inconsistent(rates)
    assert isinstance(result, bool)


def test__is_inconsistent__examples(case):
    rates = case["rates"]
    answer = case["answer"]

    result = is_inconsistent(rates)
    assert answer == result

