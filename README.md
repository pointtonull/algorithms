# Algorithms

## Check brackets in the code

In this problem you will implement a feature for a text editor to find errors in the
usage of brackets in the code.

Your friend is making a text editor for programmers. He is currently working on a
feature that will find errors in the usage of different types of brackets. Code can
contain any brackets from the set []{}(), where the opening brackets are [,{, and ( and
the closing brackets corresponding to them are ],}, and ).

For convenience, the text editor should not only inform the user that there is an error
in the usage of brackets, but also point to the exact place in the code with the
problematic bracket. First priority is to find the first unmatched closing bracket
which either doesn’t have an opening bracket before it, like ] in ](), or closes the
wrong opening bracket, like } in ()[}. If there are no such mistakes, then it should
find the first unmatched opening bracket without the corresponding closing bracket
after it, like ( in {}([]. If there are no mistakes, text editor should inform the user
that the usage of brackets is correct.

Apart from the brackets, code can contain big and small latin letters, digits and
punctuation marks. More formally, all brackets in the code should be divided into pairs
of matching brackets, such that in each pair the opening bracket goes before the
closing bracket, and for any two pairs of brackets either one of them is nested inside
another one as in (foo[bar]) or they are separate as in f(a,b)-g[c]. The bracket [
corresponds to the bracket ], { corresponds to }, and ( corresponds to ).

The implementation has to be the most efficient possible and be able to handle large
input sizes.

Solution:
- [tests](tests/test__check_brackets.py)
- [implementation](src/check_brackets.py)


# Problem of the day

## Decomposition pair

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the
list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?

Solution:
- [tests](tests/test__decomposition_pair.py)
- [implementation](src/decomposition_pair.py)

## The product of others

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i 
of the new array is the product of all the numbers in the original array except
the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
[120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be 
[2, 3, 6].

Follow-up: what if you can't use division?

Solution:
- [tests](tests/test__the_product_of_others.py)
- [implementation](src/the_product_of_others.py)


## Tree Again

This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the
tree into a string, and deserialize(s), which deserializes the string back into
the tree.

For example, given the following Node class

```Python
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
```


The following test should pass:

```Python
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
```

I decided not to take shortcuts (using custom serializer for pickle or json), but
instead implement a tailored syntax. It's not too complex and allows for a more clean
representation:

```
    root
        left
            left.left
                None
                None
            None
        right
            None
            None
```

Solution:
- [tests](tests/test__tree_again.py)
- [implementation](src/tree_again.py)


## Find The Gap

This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear
time and constant space. In other words, find the lowest positive integer that
does not exist in the array. The array can contain duplicates and negative
numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should
give 3.

You can modify the input array in-place.

Solution:
- [tests](tests/test__find_the_gap.py)
- [implementation](src/find_the_gap.py)


## Twisted Pair

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and
last element of that pair. For example, car(cons(3, 4)) returns 3, and 
cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

```Python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```


Implement car and cdr.

Solution:
- [tests](tests/test__twisted_pair.py)
- [implementation](src/twisted_pair.py)


## Xor List

This problem was asked by Google.

An XOR linked list is a more memory efficient doubly linked list. Instead of
each node holding next and prev fields, it holds a field named both, which is an
XOR of the next node and the previous node. Implement an XOR linked list; it has
an add(element) which adds the element to the end, and a get(index) which
returns the node at index.

If using a language that has no pointers (such as Python), you can assume you
have access to get_pointer anddereference_pointer functions that converts
between nodes and memory addresses(sic).

Notes:

- Actually python has support for low-level memory operations, I implemented them
  without problem and requiring only a minimal hack. The problem is that gc will free
  any non referenced object. The solution is to attach a self-reference to each node.
  The tradeof is having to delete this self-reference on removing the node, but it's
  way cleaner than messing with how gc operates or stoping gc altogheter.

- I am not implementing the interfaces as fuctions but as methods.

- `List.add` is not Pythonic, I called it `List.append`

- I added the `List.__iter__` method to allow coversion to list to better test.

- There is a iterative and a recursive implementation of traversing in this
  implementation, this is on purpose; I wanted to try both approaches.

Solution:
- [tests](tests/test__xor_list.py)
- [implementation](src/xor_list.py)
