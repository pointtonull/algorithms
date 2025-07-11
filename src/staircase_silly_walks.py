def _get_climb_combinations(steps, leaps):
    """Recursive generation for the combinations"""
    for leap in leaps:
        if leap == steps:
            yield 1
        elif leap < steps:
            yield from _get_climb_combinations(steps - leap, leaps)


def get_climb_combinations(steps, leaps):
    """
    STAIRCASE SILLY WALKS

    This problem was asked by Amazon.
    Difficulty: Hard

    There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a
    time. Given N, write a function that returns the number of unique ways you can climb
    the staircase. The order of the steps matters.

    For example, if N is 4, then there are 5 unique ways:
        * 1, 1, 1, 1
        * 2, 1, 1
        * 1, 2, 1
        * 1, 1, 2
        * 2, 2

    What if, instead of being able to climb 1 or 2 steps at a time, you could climb any
    number from a set of positive integers X?
    For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
    """
    return sum(_get_climb_combinations(steps, leaps))
