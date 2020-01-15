from typing import List


def reconstruct_sentence(words: List[str], compressed: str) -> List[str]:
    """
    This problem was asked by Microsoft.

    Given a dictionary of words and a string made up of those words (no spaces),
    return the original sentence in a list.
    If there is more than one possible reconstruction, return any of them. If
    there is no possible reconstruction, then return null.

    For example, given the set of words 'quick', 'brown', 'the', 'fox', and the
    string "thequickbrownfox", you should return ['the', 'quick', 'brown',
    'fox'].

    Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the
    string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or
    ['bedbath', 'and', 'beyond'].

    Args:
        words: List of words that can be used to reconstruct a sentence.
        compressed: The sentence without word separations.

    Returns:
        A list with sorted words for any of the possible reconstructions for
        `compressed` with the given words.

    """
    for word in words:
        if compressed.startswith(word):
            result = [word]
            rest_compressed = compressed[len(word):]
            if rest_compressed:
                rest_result = reconstruct_sentence(words, rest_compressed)
                result.extend(rest_result)
            return result