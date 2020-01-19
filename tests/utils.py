import pytest


def deep_diff(left, right, keys=[], order=True):
    """
    Allows for recursive approx comparassions.
    This is needed for acurate assesment of relevant differences in deep objects.
    """
    if left == right:
        return None

    if isinstance(left, dict):
        for key in left.keys():
            diff = deep_diff(left[key], right[key], keys + [key])
            if diff:
                return diff

    elif isinstance(left, list):
        if not order:
            left = sorted(left)
            right = sorted(right)
        for key, (left_value, right_value) in enumerate(zip(left, right)):
            diff = deep_diff(left_value, right_value, keys + [key])
            if diff:
                return diff
    else:
        try:
            if pytest.approx(left) != float(right):
                return f"sub-key `{keys}` differs: {left} != {right}"
        except TypeError:
            if left != right:
                return f"sub-key `{keys}` differs: {left} != {right}"
