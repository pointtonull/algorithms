"""MULTIPLES_GENERATOR

Define a generator which generates the positive integers up to and
including a supplied value which are divisible by another supplied positive
integer and use it to calculate the sum of all positive integers less than
102030 which are divisible by 3
"""


def multiples_generator(limit, divisor):
    yield from range(divisor, limit+1, divisor)
