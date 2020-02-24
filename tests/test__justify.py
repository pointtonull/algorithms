from pytest import fixture

from src.justify import justify, total_lenght

"""
JUSTIFY

This problem was asked by Palantir.
Dificulty: Medium

Write an algorithm to justify text. Given a sequence of words and an integerline
length k, return a list of strings which represents each line,
fully justified.

More specifically, you should have as many words as possible in each line.
Thereshould be at least one space between each word. Pad extra spaces when
necessary so that each line has exactly length k. Spaces should be distributed as
equally as possible, with the extra spaces, if any, distributed starting from the
left. If you can only fit one word on a line, then you should pad the right-hand
sidewith spaces. Each word is guaranteed not to be longer than k.

For example:
    words = ["the", "quick", "brown", "fox", "jumps","over", "the", "lazy", "dog"]
    k = 16
    you should return the following:
        [
            "the  quick brown",  # 1 extra space on the left
            "fox  jumps  over",  # 2 extra spaces distributed evenly
            "the   lazy   dog",  # 4 extra spaces distributed evenly
        ]
"""

CASES = [
    {
        "words": [
            "the",
            "quick",
            "brown",
            "fox",
            "jumps",
            "over",
            "the",
            "lazy",
            "dog",
        ],
        "k": 16,
        "answer": [
            ["the  quick brown"],  # 1 extra space on the left
            ["fox  jumps  over"],  # 2 extra spaces distributed evenly
            ["the   lazy   dog"],  # 4 extra spaces distributed evenly
        ],
    },
]


@fixture(params=CASES)
def case(request):
    return request.param


def test__total_lenght__signature():
    result = total_lenght([])
    assert isinstance(result, int)


def test__total_lenght__examples():
    result = total_lenght([])
    assert result == 0

    result = total_lenght([""])
    assert result == 0

    result = total_lenght(["1"])
    assert result == 1

    result = total_lenght(["", ""])
    assert result == 1

    result = total_lenght(["1", "2"])
    assert result == 3

    result = total_lenght(["1", "2", "3"])
    assert result == 5

    result = total_lenght(["1", "22", "333"])
    assert result == 8


def test__justify__signature(case):
    words = case["words"]
    k = case["k"]

    result = justify(words, k)
    assert isinstance(result, list)


def test__justify__examples(case):
    words = case["words"]
    k = case["k"]
    answer = case["answer"]

    result = justify(words, k)
    assert answer == result
