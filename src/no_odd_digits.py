def has_no_odd_digits(number: int) -> bool:
    while number:
        number, digit = divmod(number, 10)
        if digit % 2:
            return False
    return True
