from pytest import fixture

from utils import deep_diff


CASES = [
    {"left": [10, 15, 3, 7], "right": [10, 15, 3, 7], "order": True, "answer": None,},
    {"left": {10, 15, 3, 7}, "right": {10, 15, 3, 7}, "order": True, "answer": None,},
    {
        "left": [10, 15, 3, 7],
        "right": [10, 15, 3, 0],
        "order": True,
        "answer": "sub-key `[3]` differs: 7 != 0",
    },
]


@fixture(params=CASES)
def case(request):
    return request.param


def test__deep_diff__signature(case):
    left = case["left"]
    right = case["right"]

    result = deep_diff(left, right)
    assert type(result) in (type(None), str)


def test__deep_diff__examples(case):
    left = case["left"]
    right = case["right"]
    order = case["order"]
    answer = case["answer"]

    result = deep_diff(left, right, order=order)
    assert answer == result
