
def the_product_of_others(numbers):
    """The product of others

    Given an array of integers, return a new array such that each element at index i 
    of the new array is the product of all the numbers in the original array except
    the one at i.

    For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
    [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be 
    [2, 3, 6].

    Follow-up: what if you can't use division?
    """
    # Using division:
    # total_product = reduce(lambda a, b: a * b, numbers)
    # result = [total_product / number for number in numbers]

    pre_pos = [1]
    for num in numbers[:-1]:
        pre_pos.append(pre_pos[-1] * num)

    pos_pos = [1]
    for num in reversed(numbers[1:]):
        pos_pos.append(pos_pos[-1] * num)
    pos_pos.reverse()

    result = [pre * pos  for pre, pos in zip(pre_pos, pos_pos)]
    return result
