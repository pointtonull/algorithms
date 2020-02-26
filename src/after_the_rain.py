from typing import List


def after_the_rain(heights: List[int]) -> int:
    """
    Recursive approach to simplify accumulation without sacrificing accuracy
    on more complex examples.
    """
    tallest = 0
    tallest_pos = 0
    water = 0
    bucket = 0
    for pos, height in enumerate(heights):
        if tallest <= height:
            tallest = height
            tallest_pos = pos
            water += bucket
            bucket = 0
        else:
            bucket += tallest - height

    if tallest_pos < len(heights) - 1:
        water += after_the_rain(heights[tallest_pos + 1:])

    return water
