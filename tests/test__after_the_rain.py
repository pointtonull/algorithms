from pytest import fixture

from src.after_the_rain import after_the_rain

CASES = [
    {
        "heights": [2, 1, 2],
        "answer": 1,
    },
    {
        "heights": [3, 0, 1, 3, 0, 5],
        "answer": 8,
    },
    {
        "heights": [0, 1, 2, 3, 2, 1, 0],
        "answer": 0,
    },
    {
        "heights": [0, 1, 2, 1, 2, 1, 0],
        "answer": 1,
    },
    {
        "heights": [3, 0, 0, 2, 0, 4],
        "answer": 10,
    },
    {
        "heights": [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],
        "answer": 6,
    },
    {
        "heights": [0, 1, 2, 3],
        "answer": 0,
    },
]


@fixture(params=CASES)
def case(request):
    return request.param


def test__after_the_rain__signature(case):
    heights = case["heights"]

    result = after_the_rain(heights)
    assert isinstance(result, int)


def test__after_the_rain__examples(case):
    heights = case["heights"]
    answer = case["answer"]

    result = after_the_rain(heights)
    assert answer == result
