from math import pi
from types import GeneratorType

from pytest import approx

from src.monte_carlo_pi import monte_carlo_pi, primes

"""
MONTE CARLO PI

This problem was asked by Google.
Difficulty: Medium

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte
Carlo method.
"""


def test__monte_carlo_pi__signature():
    result = monte_carlo_pi(1)
    assert isinstance(result, float)


def test__monte_carlo_pi__examples():
    precision = 3
    epsilon = 10 ** (-precision)

    result = monte_carlo_pi(precision)

    assert pi == approx(result, abs=epsilon)


def test__primes__signature():
    result = primes()
    assert isinstance(result, GeneratorType)


def test__primes__first_examples():
    first_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23)
    for result, answer in zip(primes(), first_primes):
        assert result == answer

