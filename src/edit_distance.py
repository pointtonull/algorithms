def edit_distance(input1, input2):
    """EDIT DISTANCE

    This problem was asked by Google.
    Difficulty: Easy

    The edit distance between two strings refers to the minimum number of character
    insertions, deletions, and substitutions required to change one string to the
    other.

    For example, the edit distance between “kitten” and “sitting” is three:
    substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

    Given two strings, compute the edit distance between them.

    """
    if not (input1 and input2):
        return max(len(input1), len(input2))

    cost = 0 if input1[0] == input2[0] else 1

    return min(
        edit_distance(input1[1:], input2[1:]) + cost,
        edit_distance(input1[1:], input2) + 1,
        edit_distance(input1, input2[1:]) + 1
    )
