from pytest import fixture

from radix_search import search_text, search_eval


CASES = [
    {
        "text": "\n".join(["Hi", "250", "300"]),
        "alphabet": "0123456789- +",
        "result": ["250", "300"],
    },
]


@fixture(params=CASES)
def case(request):
    return request.param


def test__search_text__signature(case):
    result = search_text(case["text"], case["alphabet"])

    assert isinstance(result, list)


def test__search_text__basic(case):
    text = case["text"]
    alphabet = case["alphabet"]
    result = case["result"]

    obtained_result = search_text(text, alphabet)

    assert set(result) == set(obtained_result)


def test__search_eval__signature(case):
    text = case["text"]
    alphabet = case["alphabet"]

    def evaluator(word):
        return word in text

    result = search_eval(evaluator, alphabet)

    assert isinstance(result, list)


def test__search_eval__basic(case):
    text = case["text"]
    alphabet = case["alphabet"]
    result = case["result"]

    def evaluator(word):
        return word in text

    obtained_result = search_eval(evaluator, alphabet)

    assert set(result) == set(obtained_result)
