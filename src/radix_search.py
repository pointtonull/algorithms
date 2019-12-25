from typing import Text, List, Iterable, Callable
from collections import deque


def search_eval(evaluator: Callable[[Text], bool], alphabet: Iterable[Text]) -> List[Text]:
    """Search for all non overlapping combination of alphabet's symbols that are accepted by evaluator

    Args:
        evaluator Callable(word) -> bool: used to filter valid matches
        alphabet: collection of valid symbols

    Returns:
        list of all non overlapping combinations
    """

    to_right = deque([""])
    to_left = deque([])
    matches = []

    while to_right:
        partial = to_right.pop()
        has_right = False
        for atom in alphabet:
            word = partial + atom
            if evaluator(word):
                to_right.append(word)
                has_right = True
        if not has_right:
            to_left.append(partial)

    while to_left:
        partial = to_left.pop()
        has_left = False
        for atom in alphabet:
            word = atom + partial
            if evaluator(word):
                to_left.append(word)
                has_left = True
        if not has_left:
            matches.append(partial)

    return matches


def search_text(text: Text, alphabet: Iterable[Text]) -> List[Text]:
    """Search for combination of alphabet's symbols in given text"""
    def evaluator(word: Text) -> bool:
        return word in text
    matches = search_eval(evaluator, alphabet)
    return matches
