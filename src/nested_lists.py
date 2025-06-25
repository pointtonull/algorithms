from typing import List


def nested_lists(n: int) -> List[List[int]]:
    """NESTED_LISTS

    Write a function which is passed an integer, n, and returns a list of n lists such that
          f(0) returns []
          f(1) returns [[1]]
          f(2) returns [[1], [1,2]]
          f(3) returns [[1], [1,2], [1,2,3]]
    """
    return [list(range(1, i+1)) for i in range(1, n+1)]
