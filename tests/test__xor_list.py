from src.xor_list import XORList

"""
XOR LIST

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of
each node holding next and prev fields, it holds a field named both, which is an
XOR of the next node and the previous node. Implement an XOR linked list; it has
an add(element) which adds the element to the end, and a get(index) which
returns the node at index.

If using a language that has no pointers (such as Python), you can assume you
have access to get_pointer anddereference_pointer functions that converts
between nodes and memory addresses(sic).

* actually python has support for low-level memory operations
"""

def test__XORList__signature():
    xorlist = XORList()

    assert isinstance(xorlist, XORList)
    assert len(xorlist) == 0


def test__XORList__examples():
    xorlist = XORList()
    items = list("abcde")

    for lenght, item in enumerate(items):
        assert len(xorlist) == lenght
        assert xorlist.append(item) == None
        assert len(xorlist) == lenght + 1

    for pos, item in enumerate(items):
        assert xorlist[pos] == item

    assert list(xorlist) == items
