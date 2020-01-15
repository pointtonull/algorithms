import pytest

import app as src_app

WORDS = [
            ([],
             []),
            ([""],
             [[""]]),
            (["god", "dog", "cat", "tac", "know", "care", "race"],
             [["god", "dog"], ["cat", "tac"], ["know"], ["care", "race"]]),
            (["god", "dog", "cat", "tac", "know", "care"],
             [["god", "dog"], ["cat", "tac"], ["know"], ["care"]]),
            (["cod", "dog", "cat", "tac", "know", "care"],
             [["cod"], ["dog"], ["cat", "tac"], ["know"], ["care"]]),
        ]

@pytest.fixture
def app(request):
    return src_app

@pytest.fixture(params=WORDS)
def anagrams_pairs(request):
    return request.param
