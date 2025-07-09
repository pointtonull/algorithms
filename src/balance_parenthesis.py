from collections import deque

OPENING = "([{"
CLOSING = ")]}"
BRACES = OPENING + CLOSING


def are_matching(left, right):
    return (left + right) in ("()", "[]", "{}")


def is_balanced(text):
    """BALANCE PARENTHESIS

    This problem was asked by Facebook.
    Difficulty: Easy

    Given a string of round, curly, and square open and closing brackets, return
    whether the brackets are balanced (well-formed).

    For example, given the string "([])[]({})", you should return true.

    Given the string "([)]" or "((()", you should return false.
    """
    stack = deque()
    for char in text:
        if char not in BRACES:
            continue
        if char in OPENING:
            stack.append(char)
        else:
            if not stack:
                return False
            pair = stack.pop()
            if not are_matching(pair, char):
                return False
    else:
        if stack:
            return False
        else:
            return True
