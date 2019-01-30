#!/usr/bin/env python3

import random
import time


def naive(items):
    items = sorted(items)
    return items[-1] * items[-2]


def maximun_pairwise_product(items):
    first, second = 0, 0
    for item in items:
        if item > first:
            first, second = item, first
        elif item > second:
            second = item
    return first * second


def main():
    n = int(input())
    items = [int(bit) for bit in input().split()]
    assert len(items) == n
    print(maximun_pairwise_product(items))


def stress():
    random.seed(0)
    minutes = 10
    end = time.time() + minutes * 60
    while time.time() < end:
        n = random.randrange(2, 10)
        m = random.randrange(2, 10)
        items = [random.randrange(m) for i in range(n)]
        result = naive(items)
        test = maximun_pairwise_product(items)
        if result == test:
            print(".", end="")
        else:
            print()
            print(items)
            print("Expected `%d`, got `%d`." % (result, test))
            break
    else:
        print()
        print("Finished without findind error after %d minutes." % minutes)


if __name__ == '__main__':
    stress()
