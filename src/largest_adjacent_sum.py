
def largest_adjacent_sum(numbers):  # O(n) time, O(1) space
    """
    LARGEST NON-ADJACENT SUM [HARD]

    This problem was asked by Airbnb.

    Given a list of integers, write a function that returns the largest sum of
    non-adjacent numbers. Numbers can be 0 or negative. 

    Follow-up: Can you do this in O(N) time and constant space?
    """
    include = exclude = 0
    for current in numbers:
        new_exclude = max(include, exclude)
        include = exclude + current
        exclude = new_exclude
        
    return max(include, exclude)
