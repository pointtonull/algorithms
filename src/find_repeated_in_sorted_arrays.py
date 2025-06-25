from typing import List, Iterable, Generator
from heapq import merge


def _repeated(input: Iterable[int]) -> Generator:  # O(n)
    """
    Generator of repeated elements from an iterable, assumes Iterable is sorted.
    """
    prev = None
    repeated = 0
    for item in input:
        if prev is None:
            prev = item
            continue
        elif item == prev:
            if repeated == 0:
                yield item
            repeated += 1
        else:
            prev = item
            repeated = 0


def _uniq(input: Iterable[int]) -> Generator:  # O(n)
    """
    Generator of unique elements from Iterable, assumes Iterable is sorted.
    """
    prev = None
    for item in input:
        if item != prev:
            prev = item
            yield item


def find_repeated_in_sorted_arrays(input1: List[int], input2: List[int]) -> List[int]:  # O(n)
    """REPEATED IN SORTED ARRAYS

    Write a function in a language of your choice which, when passed two sorted
    arrays of integers returns an array of any numbers which appear in both. No
    value should appear in the returned array more than once.
    """
    return list(_repeated(merge(_uniq(input1), _uniq(input2))))
