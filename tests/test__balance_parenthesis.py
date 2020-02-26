from pytest import fixture

from src.balance_parenthesis import is_balanced

"""
BALANCE PARENTHESIS

This problem was asked by Facebook.
Difficulty: Easy

Given a string of round, curly, and square open and closing brackets, return
whether the brackets are balanced (well-formed).

"""

CASES = [
    {
        "text": "([])[]({})",
        "answer": True,
    },
    {
        "text": "([)]",
        "answer": False,
    },
    {
        "text": "((()",
        "answer": False,
    },
]



@fixture(params=CASES)
def case(request):
    return request.param


def test__is_balanced__signature(case):
    text = case["text"]

    result = is_balanced(text)
    assert isinstance(result, bool)


def test__is_balanced__examples(case):
    text = case["text"]
    answer = case["answer"]

    result = is_balanced(text)
    assert answer == result

