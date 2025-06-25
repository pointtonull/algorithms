from copy import copy

from pytest import fixture

from src.sort_colors_rgb import sort_colors_rgb

"""
SORT COLORS RGB

Given an array of strictly the characters 'R', 'G', and 'B', segregate
thevalues of the array so that all the Rs come first, the Gs come second, and
theBs come last.

You can only swap elements of the array.

Do this in linear time and in-place.
"""

CASES = [
    {
        "unsorted": ["G", "R"],
        "answer": ["R", "G"],
    },
    {
        "unsorted": ["B", "G", "R"],
        "answer": ["R", "G", "B"],
    },
    {
        "unsorted": ["G", "B", "R", "R", "B", "R", "G"],
        "answer": ["R", "R", "R", "G", "G", "B", "B"],
    },
    {
        "unsorted": list("GBRRBRGGBRRBRG"),
        "answer":   list("RRRRRRGGGGBBBB"),
    },
    {
        "unsorted": list("GBRRBRGGBRRBRG"*100),
        "answer":   list("RRRRRR" * 100 + "GGGG" * 100 + "BBBB" * 100),
    },
]


@fixture(params=CASES)
def case(request):
    return request.param


def test__sort_colors_rgb__signature():
    unsorted = list("RGB")

    output = sort_colors_rgb(unsorted)

    # the ordering is done in place
    assert output is None


def test__sort_colors_rgb__examples(case):
    unsorted = case["unsorted"]
    answer = case["answer"]

    work_on = copy(unsorted)

    sort_colors_rgb(work_on)

    assert answer == work_on
