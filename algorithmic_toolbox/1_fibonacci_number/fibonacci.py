from functools import lru_cache

def calc_fib_naive(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

@lru_cache()
def calc_fib_optimized(n):
    if (n <= 1):
        return n

    return calc_fib(n - 1) + calc_fib(n - 2)

