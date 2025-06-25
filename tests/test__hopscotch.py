from pytest import fixture

from src.hopscotch import hopscotch, hopscotch_varied_steps

"""
HOPSCOTCH

This problem was asked by Amazon.
Difficulty: Hard

There exists a staircase with N steps, and you can climb up either 1 or 2
steps at a time. Given N, write a function that returns the number of
unique ways you can climb the staircase. The order of the steps matters.
For example, if N is 4, then there are 5 unique ways:
* 1, 1, 1, 1
* 2, 1, 1
* 1, 2, 1
* 1, 1, 2
* 2, 2
What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
"""

CASES = [
    {
        "num_steps": 0,
        "answer": 0,
    },
    {
        "num_steps": 1,
        "answer": 1,
    },
    {
        "num_steps": 2,
        "answer": 2,
    },
    {
        "num_steps": 3,
        "answer": 3,
    },
    {
        "num_steps": 4,
        "answer": 5,
    },
    {
        "num_steps": 5,
        "answer": 8,
    },
]


@fixture(params=CASES)
def case(request):
    return request.param


def test__hopscotch__signature(case):
    num_steps = case["num_steps"]

    result = hopscotch(num_steps)
    assert isinstance(result, int)


def test__hopscotch__examples(case):
    num_steps = case["num_steps"]
    answer = case["answer"]

    result = hopscotch(num_steps)
    assert answer == result


# Test cases for the stretch goal: hopscotch with varied step sets
VARIED_STEPS_CASES = [
    {
        "num_steps": 0,
        "steps_set": {1, 3, 5},
        "answer": 1,  # One way to climb 0 steps (don't climb)
    },
    {
        "num_steps": 1,
        "steps_set": {1, 3, 5},
        "answer": 1,  # Only one way: [1]
    },
    {
        "num_steps": 2,
        "steps_set": {1, 3, 5},
        "answer": 1,  # Only one way: [1, 1]
    },
    {
        "num_steps": 3,
        "steps_set": {1, 3, 5},
        "answer": 2,  # Two ways: [1, 1, 1] or [3]
    },
    {
        "num_steps": 4,
        "steps_set": {1, 3, 5},
        "answer": 3,  # Three ways: [1, 1, 1, 1], [1, 3], [3, 1]
    },
    {
        "num_steps": 5,
        "steps_set": {1, 3, 5},
        "answer": 5,  # Five ways: [1, 1, 1, 1, 1], [1, 1, 3], [1, 3, 1], [3, 1, 1], [5]
    },
    {
        "num_steps": 6,
        "steps_set": {1, 3, 5},
        "answer": 8,  # [1,1,1,1,1,1], [1,1,1,3], [1,1,3,1], [1,3,1,1], [3,1,1,1], [3,3], [1,5], [5,1]
    },
    {
        "num_steps": 3,
        "steps_set": {2, 3},
        "answer": 1,  # Only one way: [3]
    },
    {
        "num_steps": 4,
        "steps_set": {2, 3},
        "answer": 1,  # Only one way: [2, 2]
    },
    {
        "num_steps": 5,
        "steps_set": {2, 3},
        "answer": 2,  # Two ways: [2, 3] or [3, 2]
    },
    {
        "num_steps": 7,
        "steps_set": {1, 2},
        "answer": 21,  # Should match classic hopscotch for num_steps=7 with {1,2}
    },
    {
        "num_steps": 1,
        "steps_set": {2, 3},
        "answer": 0,  # No way to climb 1 step with only {2, 3}
    },
    {
        "num_steps": 2,
        "steps_set": {3, 5},
        "answer": 0,  # No way to climb 2 steps with only {3, 5}
    },
]


@fixture(params=VARIED_STEPS_CASES)
def varied_case(request):
    return request.param


def test__hopscotch_varied_steps__signature(varied_case):
    """Test that hopscotch_varied_steps has the correct signature and returns an integer."""
    num_steps = varied_case["num_steps"]
    steps_set = varied_case["steps_set"]

    result = hopscotch_varied_steps(num_steps, steps_set)
    assert isinstance(result, int)


def test__hopscotch_varied_steps__examples(varied_case):
    """Test that hopscotch_varied_steps returns correct answers for various step sets."""
    num_steps = varied_case["num_steps"]
    steps_set = varied_case["steps_set"]
    answer = varied_case["answer"]

    result = hopscotch_varied_steps(num_steps, steps_set)
    assert answer == result
