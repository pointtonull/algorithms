from pytest import fixture

from src.maze import shortest_path

"""
MAZE

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
```

and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number
of steps required to reach the end is 7, since we would need to go through (1,2)
because there is a wall everywhere else on the second row.
"""

CASES = [
    {
        "maze": [
            [0, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        "start": (3, 0),
        "end": (0, 0),
        "answer": 7,
    },
    {
        "maze": [
            [0, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        "start": (2, 0),
        "end": (0, 0),
        "answer": 6,
    },
    {
        "maze": [
            [0, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        "start": (2, 1),
        "end": (0, 0),
        "answer": 5,
    },
    {
        "maze": [
            [0, 0, 0, 0],
            [1, 1, 1, 1],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ],
        "start": (2, 1),
        "end": (0, 0),
        "answer": None,
    },
    {
        "maze": [
            [0, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 0, 0],
            [1, 0, 1, 0],
            [0, 0, 0, 0]
        ],
        "start": (4, 0),
        "end": (0, 3),
        "answer": 7,
    },
    {
        "maze": [
            [0, 0, 0, 0],
            [0, 1, 1, 1],
            [0, 0, 0, 0],
            [1, 1, 1, 0],
            [0, 0, 0, 0]
        ],
        "start": (4, 0),
        "end": (0, 3),
        "answer": 13,
    },
]


@fixture(params=CASES)
def case(request):
    return request.param


def test__shortest_path__signature(case):
    maze = case["maze"]
    start = case["start"]
    end = case["end"]

    result = shortest_path(maze, start, end)
    assert isinstance(result, int) or result is None


def test__shortest_path__examples(case):
    maze = case["maze"]
    start = case["start"]
    end = case["end"]

    answer = case["answer"]

    result = shortest_path(maze, start, end)
    assert answer == result
