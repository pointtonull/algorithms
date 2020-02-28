from heapq import heappop, heappush, heappushpop
from bisect import insort


class Heap:

    def __init__(self, reversed=False):
        self.reversed = reversed
        self.heap = []

    def __len__(self):
        return len(self.heap)

    def push(self, item):
        if self.reversed:
            heappush(self.heap, -item)
        else:
            heappush(self.heap, item)

    def pushpop(self, item):
        if self.reversed:
            return -heappushpop(self.heap, -item)
        else:
            return heappushpop(self.heap, item)

    def peek(self):
        if self.reversed:
            return - self.heap[0]
        else:
            return self.heap[0]


def running_median_naive(sequence):
    seen = []
    for num, item in enumerate(sequence, 1):
        insort(seen, item)
        if num % 2:
            yield seen[num // 2]
        else:
            yield sum(seen[num // 2 - 1: num // 2 + 1]) / 2


def running_median(sequence):
    """RUNNING MEDIAN

    This problem was asked by Microsoft.
    Difficulty: Easy

    Compute the running median of a sequence of numbers. That is, given a stream of
    numbers, print out the median of the list so far on each new element.

    Recall that the median of an even-numbered list is the average of the two middle
    numbers.
    """
    sequence = (item for item in sequence)  # assure it's an iterator

    smallers = Heap(reversed=True)
    largers_equal = Heap()
    median = next(sequence)
    largers_equal.push(median)
    yield median

    for item in sequence:
        if item < median:
            if len(largers_equal) < len(smallers):
                largers_equal.push(smallers.pushpop(item))
            else:
                smallers.push(item)
        else:
            if len(smallers) < len(largers_equal):
                smallers.push(largers_equal.pushpop(item))
            else:
                largers_equal.push(item)

        if len(smallers) < len(largers_equal):
            median = largers_equal.peek()
        elif len(largers_equal) < len(smallers):
            median = smallers.peek()
        else:
            median = (smallers.peek() + largers_equal.peek()) / 2

        yield median
