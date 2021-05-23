""" Incrementing List of digits with 1 (one) and return again List of digits """


def add_one(arr):
    """ Takes number, and returns the incremented result

    @param arr: List of digits (representing number)
    @return: List representing number
    """
    result = []

    number = int(''.join(str(digit) for digit in arr))
    print(number)

    return result
