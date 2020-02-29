from random import Random

from pytest import fixture

from src.regexs import match, match_reference

random = Random(0)

"""
REGEXS

This problem was asked by Facebook.
Difficulty: Hard

Implement regular expression matching with the following special characters:
 
 - "." (period) which matches any single character
 - "*" (asterisk) which matches zero or more of the preceding element
 
That is, implement a function that takes in a string and a valid regular
expression and returns whether or not the string matches the regular expression.

Given the regular expression ".*at" and the string "chat", your function should return true.
The same regular expression on the string "chats" should return False.
"""

CASES = [
    {
        "regex": "ra.",
        "text": "ray",
        "answer": True,
    },
    {
        "regex": "ra.",
        "text": "raymond",
        "answer": False,
    },
    {
        "regex": ".*at",
        "text": "chat",
        "answer": True,
    },
    {
        "regex": ".*at",
        "text": "cat",
        "answer": True,
    },
    {
        "regex": ".*at",
        "text": "chats",
        "answer": False,
    },
]


@fixture(params=CASES)
def case(request):
    return request.param


@fixture(params=range(1, 30))
def case_stress(request):
    atoms = [".", ".*", "a", "b", "c"]
    regex = (random.choice(atoms) for _ in range(request.param))
    regex = "".join(regex)
    text = (random.choice(atoms[2:]) for _ in range(request.param))
    text = "".join(text)
    answer = match_reference(regex, text)
    return {"regex": regex, "text": text, "answer": answer}


def test__match__signature(case):
    regex = case["regex"]
    text = case["text"]

    result = match(regex, text)
    assert isinstance(result, bool)


def test__match__examples(case):
    regex = case["regex"]
    text = case["text"]
    answer = case["answer"]

    result = match(regex, text)
    assert answer == result


def test__match_reference__signature(case):
    regex = case["regex"]
    text = case["text"]

    result = match_reference(regex, text)
    assert isinstance(result, bool)


def test__match_reference__examples(case):
    regex = case["regex"]
    text = case["text"]
    answer = case["answer"]

    result = match_reference(regex, text)
    assert answer == result


def test__match__stress(case_stress):
    regex = case_stress["regex"]
    text = case_stress["text"]
    answer = case_stress["answer"]

    result = match(regex, text)
    assert answer == result
