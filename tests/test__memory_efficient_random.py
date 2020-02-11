from collections import Counter

from pytest import fixture

from src.memory_efficient_random import memory_efficient_random

"""
MEMORY EFFICIENT RANDOM

This problem was asked by Facebook.
Dificulty: Medium

Given a stream of elements too large to store in memory, pick a random elementfrom
the stream with uniform probability.
"""


def test__memory_efficient_random__signature():
    elements = range(10)

    result = memory_efficient_random(elements)
    assert isinstance(result, int)


def test__memory_efficient_random__examples():
    elements = range(10)

    counter = Counter(memory_efficient_random(elements)
                      for case in range(10000))

    for count in counter.values():
        assert abs(count - 1000) <= 150
