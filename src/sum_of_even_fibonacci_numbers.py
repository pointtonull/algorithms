from math import sqrt


def even_fibonacci_numbers(n: int) -> int:
    """ Second binomial transform."""
    return int(
        2 * (
            (2 + sqrt(5)) ** n
            - (2 - sqrt(5)) ** n
        ) // sqrt(20)
    )

    ## Deprecated recursive implementation
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 2
    # return 4 * even_fibonacci_numbers(n - 1) + even_fibonacci_numbers(n - 2)


def sum_of_even_fibonacci_numbers(n: int) -> int:
    """SUM OF EVEN FIBONACCI NUMBERS

    Efficient implementation of serie of partial sum of even fibonacci numbers
    based on the closed form expression of Fibonacci sequence.
    """

    return int(
        (
            (5 - 3 * sqrt(5)) * (2 - sqrt(5)) ** n
            + (2 + sqrt(5)) ** n * (5 + 3 * sqrt(5))
            - 10
        )
        // 20
    )

    ## Deprecated recursive implementation
    # if n == 0:
    #     return 0
    # if n == 1:
    #     return 2
    # return (
    #     4 * sum_of_even_fibonacci_numbers(n - 1)
    #     + sum_of_even_fibonacci_numbers(n - 2)
    #     + 2
    # )
