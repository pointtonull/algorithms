def find_the_gap(numbers):
    """FIND THE GAP

    This problem was asked by Stripe.

    Given an array of integers, find the first missing positive integer in linear
    time and constant space. In other words, find the lowest positive integer that
    does not exist in the array. The array can contain duplicates and negative
    numbers as well.

    For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
    give 3.
    """
    # Bucket sort O(n)
    seen = [False] * len(numbers)
    for num in numbers:
        if 0 < num <= len(numbers):
            seen[num - 1] = True

    for pos, val in enumerate(seen):
        if not val:
            return pos + 1
    else:
        return len(numbers) + 1
