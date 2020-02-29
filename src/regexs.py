import re


def match_reference(regex: str, text: str) -> bool:
    return bool(re.fullmatch(regex, text))


def match(regex: str, text: str):
    """REGEXS

    This problem was asked by Facebook.
    Difficulty: Hard

    Implement regular expression matching with the following special characters:

     - "." (period) which matches any single character
     - "*" (asterisk) which matches zero or more of the preceding element

    That is, implement a function that takes in a string and a valid regular
    expression and returns whether or not the string matches the regular expression.
    """
    if (not regex) and (not text):
        return True
    elif regex.startswith(".*"):
        if text:
            return any([
                match(regex, text[1:]),
                match(regex[2:], text[1:]),
                match(regex[2:], text),
            ])
        else:
            return match(regex[2:], text)
    elif regex and text:
        if regex.startswith(".") or regex.startswith(text[0]):
            return match(regex[1:], text[1:])
        else:
            return False
    else:
        return False
