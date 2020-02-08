from pytest import fixture

from src.universal_trees import count_universal_trees
from src.tree_again import deserialize

"""
COUNT UNIVERSAL TREES

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes
under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
"""

CASES = [
    {
        "tree": deserialize("\n".join((
            "0",
            "    1",
            "        None",
            "        None",
            "    0",
            "        1",
            "            1",
            "                None",
            "                None",
            "            1",
            "                None",
            "                None",
            "        0",
            "            None",
            "            None",
        ))),
        "answer": 5,
    },
    {
        "tree": deserialize("\n".join((
            "0",
            "    1",
            "    0",
            "        1",
            "            1",
            "            1",
            "        0",
        ))),
        "answer": 5,
    },
]



@fixture(params=CASES)
def case(request):
    return request.param


def test__count_universal_trees__signature(case):
    tree = case["tree"]

    result = count_universal_trees(tree)
    assert isinstance(result, int)


def test__count_universal_trees__examples(case):
    tree = case["tree"]
    answer = case["answer"]

    result = count_universal_trees(tree)
    assert answer == result

