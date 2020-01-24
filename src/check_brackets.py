from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text: str) -> int:
    """Check brackets
    
    Args:
        text: The text to be validated.
    
    Returns:
        The pos of the first error, 0 if there is no error.
    """
    opening_brackets_stack = []
    for pos, char in enumerate(text, 1):
        if char in "([{":
            opening_brackets_stack.append((pos, char))
        elif char in ")]}":
            if not opening_brackets_stack:
                stacked = " "
            else:
                _, stacked = opening_brackets_stack.pop()
            if not are_matching(stacked, char):
                return pos
    else:
        if opening_brackets_stack:
            return opening_brackets_stack[-1][0]
        return 0


def main():
    text = input()
    mismatch = find_mismatch(text)
    if not mismatch:
        print("Success")
    else:
        print(mismatch)


if __name__ == "__main__":
    main()
