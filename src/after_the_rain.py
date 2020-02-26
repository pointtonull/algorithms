from typing import List


def after_the_rain_naive(heights: List[int]) -> int:
    """
    Naive implementation for verification.
    """
    concrete = sum(heights)

    left_max = []
    current_max = 0
    for height in heights:
        current_max = max(current_max, height)
        left_max.append(current_max)

    right_max = []
    current_max = 0
    for height in reversed(heights):
        current_max = max(current_max, height)
        right_max.append(current_max)
    right_max.reverse()

    total = sum(min(left, right) for left, right in zip(left_max, right_max))
    water = total - concrete
    return water


def after_the_rain(heights: List[int]) -> int:
    """
    Simple and easy to read solution in O(n) time and O(1) memory.
    """
    tallest = 0
    tallest_pos = 0
    for pos, height in enumerate(heights):
        if tallest < height:
            tallest = height
            tallest_pos = pos

    water = 0

    # now we can use simple accumulation from left to tallest
    tallest = 0
    for height in heights[:tallest_pos]:
        if tallest < height:
            tallest = height
        else:
            water += tallest - height

    # and from right to tallest
    tallest = 0
    for height in reversed(heights[tallest_pos:]):
        if tallest < height:
            tallest = height
        else:
            water += tallest - height

    return water
