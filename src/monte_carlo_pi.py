from itertools import count, takewhile
from functools import lru_cache


@lru_cache()
def is_prime(n):
    for prime in takewhile(lambda p: p <= n ** 0.5, primes()):
        if not n % prime:
            return False
    return True


def primes():
    """ Reverse Erathostenes cribe"""
    yield from (2, 3)
    for n in count(5):
        if is_prime(n):
            yield n


def monte_carlo_pi(precision=4):
    """MONTE CARLO PI

    This problem was asked by Google.
    Dificulty: Medium

    The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a
    Monte Carlo method.
    """

    mask = 10 ** precision
    lower = 0
    upper = 0
    total = 0

    for resolution in primes():
        total += resolution ** 2
        row = resolution - 1
        for col in range(resolution):
            x = (col + 0.5) / resolution
            while 1 <= (x**2 + ((row + 0.5) / resolution)**2) ** 0.5:
                row -= 1
            lower += row + 0.5
            upper += row + 1

        lower_pi = lower / total * 4
        upper_pi = upper / total * 4
        if lower < upper and int(lower_pi * mask) == int(upper_pi * mask):
            return (lower_pi + upper_pi) / 2
