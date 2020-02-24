def total_lenght(words):
    chars = sum(len(word) for word in words)
    word_sep = max(0, len(words) - 1)
    return chars + word_sep


def justify_line(words, lenght=40):
    total = total_lenght(words)
    if lenght < total_lenght:
        raise ValueError(f"words' total lenght is greater than allowed lenght.")
    extra_spaces = lenght - total



def justify(words, lenght=40):
    """JUSTIFY

    Write an algorithm to justify text. Given a sequence of words and an integerline
    length k, return a list of strings which represents each line,
    fully justified.

    More specifically, you should have as many words as possible in each line.
    Thereshould be at least one space between each word. Pad extra spaces when
    necessary so that each line has exactly length k. Spaces should be distributed as
    equally as possible, with the extra spaces, if any, distributed starting from the
    left. If you can only fit one word on a line, then you should pad the right-hand
    sidewith spaces. Each word is guaranteed not to be longer than k.

    For example:
        words = ["the", "quick", "brown", "fox", "jumps","over", "the", "lazy", "dog"]
        k = 16
        you should return the following:
            [
                "the  quick brown",  # 1 extra space on the left
                "fox  jumps  over",  # 2 extra spaces distributed evenly
                "the   lazy   dog",  # 4 extra spaces distributed evenly
            ]
    """

    result = []
    current_line = []

    for word in words:
        new_lenght = total_lenght(current_line) + len(word) + 1
        if lenght < new_lenght:
            result.append(current_line)
            current_line = []
        current_line.append(word)

    result.append(current_line)
    return result
