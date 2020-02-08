from pytest import fixture

from src.staircase_silly_walks import get_climb_combinations


CASES = [
    {
        "steps": 0,
        "leaps": {1},
        "answer": 0,  # there is no solution
    },
    {
        "steps": 4,
        "leaps": {1},
        "answer": 1,
    },
    {
        "steps": 4,
        "leaps": {1, 2},
        "answer": 5,
    },
]


@fixture(params=CASES)
def case(request):
    return request.param


def test__get_climb_combinations__signature(case):
    steps = case["steps"]
    leaps = case["leaps"]

    result = get_climb_combinations(steps, leaps)
    assert isinstance(result, int)


def test__get_climb_combinations__examples(case):
    steps = case["steps"]
    leaps = case["leaps"]
    answer = case["answer"]

    result = get_climb_combinations(steps, leaps)
    assert answer == result

