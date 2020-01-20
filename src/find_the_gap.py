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

    # Nullify any invalid numbers
    for pos, num in enumerate(numbers):
        if num <= 0:
            numbers[pos] = len(numbers) + 2 # imposible high

    # Bucket set
    for num in numbers:
        if abs(num) <= (len(numbers) + 1):
            num = abs(num)
            pos = num - 1
            numbers[pos] = -abs(numbers[pos])

    # first positive marker is the index1 pos
    for pos, val in enumerate(numbers):
        if 0 < val:
            return pos + 1
    else:
        return len(numbers) + 1


if __name__ == "__main__":
    find_the_gap([3, 4, -6, -1])
