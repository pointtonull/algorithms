from typing import Tuple, List
from collections import deque

NEIGHBOURS = ((-1, 0), (0, -1), (0, 1), (1, 0))


def shortest_path(maze: List[List[int]], start: Tuple[int], end: Tuple[int]) -> int:
    """MAZE

    This problem was asked by Google.
    Difficulty: Easy

    You are given an M by N matrix consisting of booleans that represents a board.
    Each True boolean represents a wall. Each False boolean represents a tile you
    can walk on.

    Given this matrix, a start coordinate, and an end coordinate, return the minimum
    number of steps required to reach the end coordinate from the start. If there is
    no possible path, then return None. You can move up, left, down, and right. You
    cannot move through walls. You cannot wrap around the edges of the board.

    For example, given the following board:
    ``` Python
        [[0, 0, 0, 0],
         [1, 1, 0, 1],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]
    ```

    and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number
    of steps required to reach the end is 7, since we would need to go through (1,2)
    because there is a wall everywhere else on the second row.
    """
    queue = deque()
    row, col = start
    queue.append((0, row, col))
    seen = set()
    while queue:
        distance, row, col = queue.popleft()
        if (row, col) == end:
            return distance
        for row_offset, col_offset in NEIGHBOURS:
            new_row, new_col = max(0, row + row_offset), max(0, col + col_offset)
            if (new_row, new_col) in seen:
                continue
            seen.add((new_row, new_col))
            try:
                if not maze[new_row][new_col]:
                    queue.append((distance + 1, new_row, new_col))
            except IndexError:
                continue
