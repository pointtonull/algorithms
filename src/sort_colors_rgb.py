from collections import Counter


def sort_colors_rgb(flags):
    """SORT COLORS RGB

    Given an array of strictly the characters 'R', 'G', and 'B', segregate
    the values of the array so that all the Rs come first, the Gs come second,
    and the Bs come last.

    You can only swap elements of the array.

    Do this in linear time and in-place.
    """
    # since it is requested we solve it in o(n), we know immediately it is not a comparative sort

    counter = Counter(flags)

    def swap(pos1, pos2):
        flags[pos1], flags[pos2] = flags[pos2], flags[pos1]

    for pos, flag in enumerate(flags):
        print(f"{pos=} {flags[pos]} {flags=}")
        if pos < counter["R"]:
            should_be = "R"
        elif pos < counter["R"] + counter["G"]:
            should_be = "G"
        else:
            should_be = "B"

        if flag != should_be:
            for pos2, flag2 in enumerate(flags[pos + 1 :], pos + 1):
                if flag2 == should_be:
                    swap(pos, pos2)
                    break
        print(f"{pos=} {flags[pos]} {flags=}\n")
