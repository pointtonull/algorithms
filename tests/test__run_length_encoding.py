from pytest import fixture

from src.run_length_encoding import encode

"""
RUN-LENGTH ENCODING

This problem was asked by Amazon.
Difficulty: Easy

Run-length encoding is a fast and simple method of encoding strings. The basic
idea is to represent repeated successive characters as a single count and
character.

For example, the string "AAAABBBCCDAA" would be encoded as"4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be
encoded have no digits and consists solely of alphabetic characters. You can
assume the string to be decoded is valid.
"""

CASES = [
    {
        "original": "AAAABBBCCDAA",
        "answer": "4A3B2C1D2A",
    },
]



@fixture(params=CASES)
def case(request):
    return request.param


def test__encode__signature(case):
    original = case["original"]

    result = encode(original)
    assert isinstance(result, str)


def test__encode__examples(case):
    original = case["original"]
    answer = case["answer"]

    result = encode(original)
    assert answer == result

