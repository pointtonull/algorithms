"""
Example thingy
"""

from collections import defaultdict


def hash_anagram(word) -> str:
    return "".join(sorted(word))


def group_anagrams(words: list) -> list:
    """
    Given a collection of words, return a list of lists where each inner list
    contains all anagrams.

    >>> group_anagrams(["god", "dog", "good", "cat"])
    [["god", "dog"], ["good"], ["cat"]]
    """
    groups = defaultdict(list)
    for word in words:
        groups[hash_anagram(word)].append(word)
    return list(groups.values())
