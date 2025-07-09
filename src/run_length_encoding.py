def encode(original):
    """RUN-LENGTH ENCODING

    This problem was asked by Amazon.
    Difficulty: Easy

    Run-length encoding is a fast and simple method of encoding strings. The basic
    idea is to represent repeated successive characters as a single count and
    character.

    For example, the string "AAAABBBCCDAA" would be encoded as"4A3B2C1D2A".

    Implement run-length encoding and decoding. You can assume the string to be
    encoded have no digits and consists solely of alphabetic characters. You can
    assume the string to be decoded is valid.
    """
    if len(original) == 0:
        return ""
    elif len(original) == 1:
        return "1" + original

    encoded = ""
    sub = original[0]
    for char in original[1:]:
        if char == sub[0]:
            sub += char
        else:
            encoded += f"{len(sub)}{sub[0]}"
            sub = char
    encoded += f"{len(sub)}{sub[0]}"
    return encoded
