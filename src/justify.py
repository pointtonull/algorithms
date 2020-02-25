from math import ceil


def total_length(words):
    chars = sum(len(word) for word in words)
    word_sep = max(0, len(words) - 1)
    return chars + word_sep


def justify_line(words, length=40):
    spaces = length - sum(len(word) for word in words)
    line = ""
    while words:
        word = words.pop(0)
        line += word
        if words:
            sep = ceil(spaces / len(words))
            line += sep * " "
            spaces -= sep
    return line


def justify(words, length=40):
    result = []
    current_line = []

    for word in words:
        new_length = total_length(current_line) + len(word) + 1
        if length < new_length:
            result.append(justify_line(current_line, length))
            current_line = []
        current_line.append(word)

    result.append(justify_line(current_line, length))
    return result
