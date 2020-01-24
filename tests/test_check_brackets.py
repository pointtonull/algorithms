from pytest import fixture

from utils import deep_diff

from src.check_brackets import find_mismatch

CASES = [
    {"text": "", "answer": 0},
    {"text": "[]", "answer": 0},
    {"text": "()", "answer": 0},
    {"text": "{}", "answer": 0},
    {"text": "{}[]{}", "answer": 0},
    {"text": "{[]}()", "answer": 0},
    {"text": "[{{}}]", "answer": 0},
    {"text": "{[}", "answer": 3},
    {"text": "[(]", "answer": 3},
    {"text": "(){[}", "answer": 5},
    {"text": "{}{}]", "answer": 5},
    {"text": "[]({)", "answer": 5},
    {"text": "[](()", "answer": 3},
    {"text": "(({})", "answer": 1},
    {"text": "({})}", "answer": 5},
    {"text": "[({])}", "answer": 4},
    {"text": "ablabla)ihihi(ohoho", "answer": 8},
    {"text": "ablab(a)ihihi(ohoh)", "answer": 0},
    {"text": "[very(strong]test)", "answer": 13},
]


@fixture(params=CASES)
def case(request):
    return request.param


def test__find_mismatch__signature(case):
    text = case["text"]

    result = find_mismatch(text)
    assert isinstance(result, int)


def test__find_mismatch__examples(case):
    text = case["text"]
    answer = case["answer"]

    result = find_mismatch(text)
    assert answer == result
