from pytest import fixture

from src.reconstruct_sentence import reconstruct_sentence


CASES = [
    {
        "words": ["quick", "brown", "the", "fox"],
        "compressed": "thequickbrownfox",
        "results": [["the", "quick", "brown", "fox"]],
    },
    {
        "words": ["bed", "bath", "bedbath", "and", "beyond"],
        "compressed": "bedbathandbeyond",
        "results": [["bed", "bath", "and", "beyond"], ["bedbath", "and", "beyond"]],
    },
]


@fixture(params=CASES)
def case(request):
    return request.param


def test__reconstruct_sentence__signature(case):
    words = case["words"]
    compressed = case["compressed"]

    result = reconstruct_sentence(words, compressed)
    assert isinstance(result, list)

    result = reconstruct_sentence(words=words, compressed=compressed)
    assert isinstance(result, list)


def test__reconstruct_sentence__given_examples(case):
    words = case["words"]
    compressed = case["compressed"]
    results = case["results"]

    result = reconstruct_sentence(words, compressed)
    assert result in results
