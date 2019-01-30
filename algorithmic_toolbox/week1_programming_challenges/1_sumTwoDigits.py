#!/usr/bin/env python3

def sum_a_b(a, b):
    return a + b

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(sum_a_b(a, b))
