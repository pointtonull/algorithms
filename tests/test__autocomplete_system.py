from pytest import fixture

from utils import deep_diff

from src.autocomplete_system import autocomplete_system, Trie

"""
AUTOCOMPLETE SYSTEM

This problem was asked by Twitter.
Difficulty: Medium

Implement an autocomplete system. That is, given a query string s and a set of all
possible query strings, return all strings in the set that have s as aprefix. For
example, given the query string "de" and the set of strings [dog, deer, deal], return
[deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure tospeed
up queries.
"""

CASES = [
    {
        "symbols": ["dog", "deer", "deal"],
        "query": "de",
        "answer": ["deer", "deal"]
    },
    {
        "symbols": ["dog", "deer", "deal"],
        "query": "",
        "answer": ["dog", "deer", "deal"]
    },
    {
        "symbols": ["dog", "deer", "deal"],
        "query": "do",
        "answer": ["dog"]
    },
]



@fixture(params=CASES)
def case(request):
    return request.param


def test__autocomplete_system__signature(case):
    symbols = case["symbols"]
    query = case["query"]

    result = autocomplete_system(symbols, query)
    assert isinstance(result, list)


def test__autocomplete_system__examples(case):
    symbols = case["symbols"]
    query = case["query"]
    answer = case["answer"]

    result = autocomplete_system(symbols, query)

    assert not deep_diff(answer, result, order=False)


def test__Trie__population(case):
    symbols = case["symbols"]
    answer = len(symbols)

    trie = Trie(symbols)
    result = len(list(trie._all_leaves()))

    assert result == answer
