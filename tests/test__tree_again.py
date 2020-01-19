from pytest import fixture

from utils import deep_diff

from src.tree_again import serialize, deserialize, Node

"""
TREE AGAIN

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the
tree into a string, and deserialize(s), which deserializes the string back into
the tree.
"""


def test__serialize__signature():
    tree = Node('root', Node('left', Node('left.left')), Node('right'))

    pickled = serialize(tree)
    assert isinstance(pickled, str)

    tree_again = deserialize(pickled)
    assert isinstance(tree_again, Node)


def test__serialize__examples():
    tree = Node('root', Node('left', Node('left.left')), Node('right'))

    pickled = serialize(tree)
    result = "\n".join((
        "root",
        "    left",
        "        left.left",
        "            None",
        "            None",
        "        None",
        "    right",
        "        None",
        "        None",
    ))
    assert pickled == result

    tree_again = deserialize(pickled)
    assert tree == tree_again
    assert tree_again.left.left.val == 'left.left'

