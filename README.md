This is a complete coverage playground repo I use as template for my tdd projects and
I maintain updated solving popular coding challenges once in a while.

# Data Structures

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

If using a language that has no pointers (such as Python)(sic), you can assume you
have access to get_pointer and dereference_pointer functions that converts
between nodes and memory addresses(sic).

Notes:

- Actually python has support for low-level memory operations, I implemented them
without problem and requiring only a minimal hack; gc will free any non referenced
object. The solution is to attach a self-reference to each node. The tradeof is
having to delete this self-reference on removing the node, but it's way cleaner than
messing with how gc operates or stoping gc altogheter.

- I am not implementing the interfaces as fuctions but as methods.

- `List.add` is not Pythonic, I called it `List.append`

- I added the `List.__iter__` method to allow coversion to list to better test.

- There is a iterative and a recursive implementation of traversing in this
  implementation, this is on purpose; I wanted to try both approaches.

Solution:
- [tests](tests/test__xor_list.py)
- [implementation](src/xor_list.py)


## Uncertain Decoder

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa',
'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not
allowed.

Solution:
- [tests](tests/test__uncertain_decoder.py)
- [implementation](src/uncertain_decoder.py)


## Count Universal Trees

This problem was asked by Google.

A unival tree (which stands for "universal value") is a tree where all nodes
under it have the same value.

Given the root to a binary tree, count the number of unival subtrees.

For example, the following tree has 5 unival subtrees:

```
   0
  / \
 1   0
    / \
   1   0
  / \
 1   1
```

Solution:
- [tests](tests/test__universal_trees.py)
- [implementation](src/universal_trees.py)


## Largest Non-Adjacent Sum

This problem was asked by Airbnb.
Difficulty: Hard

Given a list of integers, write a function that returns the largest sum of
non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1,
1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?

Solution:
- [tests](tests/test__largest_adjacent_sum.py)
- [implementation](src/largest_adjacent_sum.py)


## Simple Job Scheduler

This problem was asked by Apple.
Difficulty: Medium

Implement a job scheduler which takes in a function `f` and an integer n, and calls f
after n milliseconds.

N.B.: I guess this is more of a challenge in other languages..., still, I decided to
keep the high level implementation in Python because this in one of the most
overseenmodules in the standar library.

Solution:
- [tests](tests/test__simple_job_scheduler.py)
- [implementation](src/simple_job_scheduler.py)


## Staircase Silly Walks

This problem was asked by Amazon.
Difficulty: Hard

There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a
time. Given N, write a function that returns the number of unique ways you can climb
the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

- 1, 1, 1, 1
- 2, 1, 1
- 1, 2, 1
- 1, 1, 2
- 2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any
number from a set of positive integers X?
For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.

Solution:
- [tests](tests/test__staircase_silly_walks.py)
- [implementation](src/staircase_silly_walks.py)


## Autocomplete System

This problem was asked by Twitter.
Difficulty: Medium

Implement an autocomplete system. That is, given a query string s and a set ofall
possible query strings, return all strings in the set that have s as aprefix. For
example, given the query string de and the set of strings [dog, deer, deal], return
[deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure tospeed
up queries.

Solution:
- [tests](tests/test__autocomplete_system.py)
- [implementation](src/autocomplete_system.py)


## Memory Efficient Random

This problem was asked by Facebook.
Difficulty: Medium

Given a stream of elements too large to store in memory, pick a random elementfrom
the stream with uniform probability.

Solution:
- [tests](tests/test__memory_efficient_random.py)
- [implementation](src/memory_efficient_random.py)


## Monte Carlo Pi

This problem was asked by Google.
Difficulty: Medium

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

I increased speed using non-overlaping diagonals to define the points. (based on prime numbers)

Solution:
- [tests](tests/test__monte_carlo_pi.py)
- [implementation](src/monte_carlo_pi.py)


## Justify

This problem was asked by Palantir.
Difficulty: Medium

Write an algorithm to justify text. Given a sequence of words and an integerline
length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line.
Thereshould be at least one space between each word. Pad extra spaces when necessary
so that each line has exactly length k. Spaces should be distributed as equally as
possible, with the extra spaces, if any, distributed starting from the left. If you
can only fit one word on a line, then you should pad the right-hand sidewith spaces.
Each word is guaranteed not to be longer than k.

For example:
    words = ["the", "quick", "brown", "fox", "jumps","over", "the", "lazy", "dog"]
    k = 16
    you should return the following:
        [
            "the  quick brown",  # 1 extra space on the left
            "fox  jumps  over",  # 2 extra spaces distributed evenly
            "the   lazy   dog",  # 4 extra spaces distributed evenly
        ]

Solution:
- [tests](tests/test__justify.py)
- [implementation](src/justify.py)


## After The Rain

This problem was asked by Facebook.
Difficulty: Medium

You are given an array of non-negative integers that represents a
two-dimensional elevation map where each element is unit-width wall and the
integer is the height. Suppose it will rain and all spots between two walls get
filled up.

Compute how many units of water remain trapped on the map in O(N) time and O(1)
space.

For example:
    - given the input [2, 1, 2], we can hold 1 unit of water in the middle.
    - given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index,
        2 in the second, and 3 in the fourth index (we cannot hold 5 since it
        would run off to the left), so we can trap 8 units of water.

I added a stress test case fixture to ensure compliance in large arrays.

Solution:
- [tests](tests/test__after_the_rain.py)
- [implementation](src/after_the_rain.py)


## Edit Distance

This problem was asked by Google.
Difficulty: Easy

The edit distance between two strings refers to the minimum number of character
insertions, deletions, and substitutions required to change one string to the
other.

For example, the edit distance between “kitten” and “sitting” is three:
substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.

Given two strings, compute the edit distance between them.

Solution:
- [tests](tests/test__edit_distance.py)
- [implementation](src/edit_distance.py)


## Run-Lenght Encoding

This problem was asked by Amazon.
Difficulty: Easy

Run-length encoding is a fast and simple method of encoding strings. The basic
idea is to represent repeated successive characters as a single count and
character.

For example, the string "AAAABBBCCDAA" would be encoded as"4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be
encoded have no digits and consists solely of alphabetic characters. You can
assume the string to be decoded is valid.

Solution:
- [tests](tests/test__run_lenght_encoding.py)
- [implementation](src/run_lenght_encoding.py)


## Balance Parenthesis

This problem was asked by Facebook.
Difficulty: Easy

Given a string of round, curly, and square open and closing brackets, return
whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.

Solution:
- [tests](tests/test__balance_parenthesis.py)
- [implementation](src/balance_parenthesis.py)



## Currency Arbitrage

This problem was asked by Jane Street.
Difficulty: Hard

Suppose you are given a table of currency exchange rates, represented as a 2D
array. Determine whether there is a possible arbitrage: that is, whether there
is some sequence of trades you can make, starting with some amount A of any
currency, so that you can end up with some amount greater than A of that currency.
There are no transaction costs and you can trade fractional quantities.

Solution:
- [tests](tests/test__currency_arbitrage.py)
- [implementation](src/currency_arbitrage.py)
