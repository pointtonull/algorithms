#!/usr/bin/env python
# -*- coding: utf-8 -*-

from array import ArrayType
import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)   # new thread will get stack of such size


class TreeHeight:

    def read(self):
        self.n = int(sys.stdin.readline())
        self.parents = ArrayType("l", (int(w) for w in
                                       sys.stdin.readline().split()))
        self.heights = ArrayType("l", (0 for p in self.parents))

    def height(self, node):
        if not self.heights[node]:
            parent = self.parents[node]
            self.heights[node] = self.height(parent)

        if self.heights[node] == 1:
            return 1

    def compute_height(self):
        heights = ArrayType("h", [0] * self.n)
        pending = [(node, parent) for node, parent in enumerate(self.parent)]
        while pending:
            postponed = []
            for node, parent in pending:
                if parent == -1:
                    heights[node] = 1
                elif heights[parent]:
                    heights[node] = heights[parent] + 1
                else:
                    postponed.append((node, parent))
            pending = postponed
        return max(heights)


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()
