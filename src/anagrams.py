import string
from functools import reduce
from operator import mul
from collections import defaultdict

LETTER_PRIME = dict(
    zip(
        string.ascii_letters,
        (
            2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71,
            73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151,
            157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233,
            239,
        ),
    )
)

def anagram_hash(word):
    """
    > anagram_hash('cat')
    710
    > anagram_hash('tac')
    710
    > anagram_hash('dog')
    5593
    > anagram_hash('Nan' * 10 + Batman)
    28470819877476016224161459901545001110315528646656
    """
    return reduce(mul, (LETTER_PRIME[c] for c in word))


# Now you have a O(1) hash function you use the map approach
# No further change is required since in python hash(integer) == integer


def group_anagrams(words):  # O(n)
    """
    Given a list of strings, write a function to return all subsets of the strings
    that are anagrams (e.g. "rope" == "pore", "fairy tales" == "rail safety").
    For example:
    ["apple", "rope", "cat", "tac", "atc", "pore"]
    -> [["apple"], ["rope", "pore"], ["cat", "tac", "atc"]]
    ["deer", "red", "reed", "cat"]
    -> [["deer", "reed"], ["red"], ["cat"]]

    This is not the simplest solution but just a implementation reference for primes approach.
    """

    groups = defaultdict(list)
    for word in words:  # O(n)
        groups[anagram_hash(word)].append(word)  # O(1)
    return list(groups.values())  # O(n)


print(group_anagrams(["apple", "rope", "cat", "tac", "atc", "pore"]))
