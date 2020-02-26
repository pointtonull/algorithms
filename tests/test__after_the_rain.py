from random import Random

from pytest import fixture

from src.after_the_rain import after_the_rain_naive, after_the_rain

random = Random(0)


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
    {
        "heights": [6, 0, 5, 4, 5],
        "answer": 6,
    },
]


@fixture(params=CASES)
def case(request):
    return request.param


@fixture(params=range(200))
def stress_case(request):
    heights = [random.randrange(10) for _ in range(request.param)]
    answer = after_the_rain_naive(heights)
    yield {"heights": heights, "answer": answer}


def test__after_the_rain__signature(case):
    heights = case["heights"]

    result = after_the_rain(heights)
    assert isinstance(result, int)


def test__after_the_rain__examples(case):
    heights = case["heights"]
    answer = case["answer"]

    result = after_the_rain(heights)
    assert answer == result


def test__after_the_rain_naive__examples(case):
    heights = case["heights"]
    answer = case["answer"]

    result = after_the_rain_naive(heights)

    assert answer == result


def test__after_the_rain__stress(stress_case):
    heights = stress_case["heights"]
    answer = stress_case["answer"]

    result = after_the_rain(heights)

    assert answer == result

