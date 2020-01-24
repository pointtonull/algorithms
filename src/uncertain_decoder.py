from typing import Text
from functools import lru_cache
import string

ENCODER = {str(pos): char for pos, char in enumerate(string.ascii_lowercase, 1)}


@lru_cache()
def possible_combinations(message: Text) -> int:
    """UNCERTAIN DECODER

    This problem was asked by Facebook.

    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
    number of ways it can be decoded.

    For example, the message '111' would give 3, since it could be decoded as 'aaa',
    'ka', and 'ak'.

    You can assume that the messages are decodable. For example, '001' is not
    allowed.
    """
    result = 0
    if not message:
        return 1
    for ebit in ENCODER:
        if message.startswith(ebit):
            result += possible_combinations(message[len(ebit) :])
    return result
