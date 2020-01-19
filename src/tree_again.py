import re
from textwrap import dedent


INDENTATION = "    "
RE_TREE = re.compile(
    r"^(?P<val>\w.*?)\n(?P<left>{}\w.*?)\n(?P<right>{}\w.*)".format(
        INDENTATION, INDENTATION
    ),
    re.S,
)

"""TREE AGAIN

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the
tree into a string, and deserialize(s), which deserializes the string back into
the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __eq__(l, r):
        if isinstance(r, Node):
            return l.val == r.val and l.left == r.left and l.right == r.right
        else:
            return False


def serialize(tree, indent=0):
    """
    I decided to do the hard work and implement a custom, compact format instead of doing the easy thing (converting to dict and json). The advantage is, the format is clean and easy to read:
        root
            left
                left.left
                    None
                    None
                None
            right
                None
                None
    """
    if tree is None:
        return INDENTATION * indent + "None"
    return "\n".join(
        (
            INDENTATION * indent + tree.val,
            serialize(tree.left, indent + 1),
            serialize(tree.right, indent + 1),
        )
    )


def deserialize(pickled):
    if pickled == "None":
        return None
    else:
        match = RE_TREE.match(pickled)
        val = match["val"]
        left = deserialize(dedent(match["left"]))
        right = deserialize(dedent(match["right"]))
        return Node(val, left, right)
