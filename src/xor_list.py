import ctypes


def dereference_pointer(obj_id: int):
    """From id to original obj
    
    Allows for low level reference management.
    Bear in mind there must be a reference to the instance at any time of the gc will
    collect it. An easy way to achieve this is adding a self reference to any object we
    want the gc to ignore.
    
    Args:
        obj_id: virual memory address

    Returns:
        The referenced object
    
    Raises:
        SegFaultError: when trying to access unbound addresses
    """
    if obj_id == 0:
        return None
    return ctypes.cast(obj_id, ctypes.py_object).value


class Node:
    """Node dataclass
    
    Very basic dataclass that implements the circular-reference hack that prevents GC
    of deleting this weakly reference nodes.
    
    Attributes:
        value: the object to be stored
        _both: left ^ right
    """

    def __init__(self, value, both=0):
        """
        Args:
            value: Any object to be stored
            both: XOR of left and right pointers
        """
        self.value = value
        self._both = both
        self.__ref = self  # circular ref prevents gc of cleaning

    def next(self, prev_id: int, steps: int):
        """recursive implementation of get(nth)
        
        Args:
            prev_id: pointer to "previous" object in the iteration. Where what
                "previous" means depends on the direction of the search.
            steps: guardian for the relative position of desired element.
                to fetch.
        
        Returns:
            The element in nth position.
        """
        if steps == 0:
            return self.value

        next_id = prev_id ^ self._both
        next_obj = dereference_pointer(next_id)
        return next_obj.next(id(self), steps - 1)


class XORList:
    def __init__(self):
        """XOR LIST

        This problem was asked by Google.

        An XOR linked list is a more memory efficient doubly linked list. Instead of
        each node holding next and prev fields, it holds a field named both, which is an
        XOR of the next node and the previous node. Implement an XOR linked list; it has
        an add(element) which adds the element to the end, and a get(index) which
        returns the node at index.

        N.B.: actually, Python has pointers.
        """
        self.start = None
        self.end = None
        self._len = 0

    def append(self, item):
        """Appends object to the end of the list."""
        new_node = Node(item)
        if self._len == 0:
            self.start = self.end = new_node
        else:
            new_node._both ^= id(self.end)
            self.end._both ^= id(new_node)
            self.end = new_node

        self._len += 1

    def __len__(self):
        """Dunder for len(xorlist)"""
        return self._len

    def __getitem__(self, index):
        """Dunder for xorlist[n]
        
        Returns: element in nth position of the list

        Raises:
            IndexError: if index larger than len - 1
            NotImplementedError: if index smaller than 0
        """
        if index < 0:
            raise NotImplementedError("It'll be easy to implement... but, reasons.")
        elif self._len <= index:
            raise IndexError(
                f"Tried to access index[{index}] outside this list limits."
            )
        return self.start.next(0, index)

    def __iter__(self):
        """Dunder for list(xorlist)"""
        prev_id = 0
        node = self.start
        while node:
            yield node.value
            obj_id = node._both ^ prev_id
            prev_id = id(node)
            node = dereference_pointer(obj_id)
