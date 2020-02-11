from random import Random
random = Random(0)


def memory_efficient_random(elements):
    """MEMORY EFFICIENT RANDOM

    This problem was asked by Facebook.
    Dificulty: Medium

    Given a stream of elements too large to store in memory, pick a random
    element from the stream with uniform probability.
    """
    for total, element in enumerate(elements, 1):
        probability = 1 / total
        if random.random() <= probability:
            choosen = element
    return choosen
