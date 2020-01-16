from pytest import fixture

from anagrams import group_anagrams
from utils import deep_diff


GROUP_ANAGRAMS_CASES = [
    {
        "words": ["apple", "rope", "cat", "tac", "atc", "pore"],
        "grouped_anagrams": [["apple"], ["rope", "pore"], ["cat", "tac", "atc"]],
    },
    {
        "words": ["deer", "red", "reed", "cat"],
        "grouped_anagrams": [["deer", "reed"], ["red"], ["cat"]],
    },
    {
        "words": ["deer", "red", "reed", "cat"],
        "grouped_anagrams": [["deer", "reed"], ["red"], ["cat"]],
    },
    {
        "words": ["deer", "red", "reed", "cat"],
        "grouped_anagrams": [["deer", "reed"], ["red"], ["cat"]],
    },
    {
        "words": ["god", "dog", "cat", "tac", "know", "care", "race"],
        "grouped_anagrams": [["god", "dog"], ["cat", "tac"], ["know"], ["care", "race"]],
    },
    {
        "words": ["god", "dog", "cat", "tac", "know", "care"],
        "grouped_anagrams": [["god", "dog"], ["cat", "tac"], ["know"], ["care"]],
    },
    {
        "words": ["cod", "dog", "cat", "tac", "know", "care"],
        "grouped_anagrams": [["cod"], ["dog"], ["cat", "tac"], ["know"], ["care"]],
    }
]


@fixture(params=GROUP_ANAGRAMS_CASES)
def case(request):
    return request.param


def test__group_anagrams__signature(case):
    words = case["words"]

    result = group_anagrams(words)
    assert isinstance(result, list)

    result = group_anagrams(words=words)
    assert isinstance(result, list)


def test__group_anagrams__given_examples(case):
    words = case["words"]
    grouped_anagrams = case["grouped_anagrams"]

    result = group_anagrams(words)
    assert not deep_diff(grouped_anagrams, result)
