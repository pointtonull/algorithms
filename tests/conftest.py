import pytest

import app as src_app

WORDS = [
            ([],
             []),
            ([""],
             [[""]]),
        ]

@pytest.fixture
def app(request):
    return src_app

@pytest.fixture(params=WORDS)
def anagrams_pairs(request):
    return request.param
