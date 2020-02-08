from src.tree_again import Node


def count_universal_trees(tree: Node):
    """COUNT UNIVERSAL TREES

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
    first, rest = _count_universal_trees(tree)
    return first + rest


def _count_universal_trees(tree):
    left, right = tree.left, tree.right
    if left is None:
        left_good = tree.val
        left_count = 0
    else:
        left_good, left_count = _count_universal_trees(left)
        if left_good is True:
            left_good = left.val

    if right is None:
        right_good = tree.val
        right_count = 0
    else:
        right_good, right_count = _count_universal_trees(right)
        if right_good is True:
            right_good = right.val

    sub_count = left_count + right_count

    if left_good == right_good == tree.val:
        tree_good = True
        sub_count += 1
    else:
        tree_good = False

    return tree_good, sub_count
