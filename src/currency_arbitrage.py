from itertools import permutations


def all_permutations(rates):
    for length in range(2, len(rates) + 1):
        for sequence in permutations(range(len(rates)), length):
            yield sequence


def execute(sequence, rates):
    amount = 1
    current_symbol = sequence[0]
    sequence = *sequence[1:], sequence[0]
    for next_symbol in sequence:
        rate = rates[current_symbol][next_symbol]
        amount *= rate
        current_symbol = next_symbol
    return amount


def is_inconsistent(rates):
    """CURRENCY ARBITRAGE

    This problem was asked by Jane Street.
    Difficulty: Hard

    Suppose you are given a table of currency exchange rates, represented as a 2D
    array. Determine whether there is a possible arbitrage: that is, whether there
    is some sequence of trades you can make, starting with some amount A of any
    currency, so that you can end up with some amount greater than A of that currency.
    There are no transaction costs and you can trade fractional quantities.
    """
    for sequence in all_permutations(rates):
        if 1 < execute(sequence, rates):
            return True
    return False
