def total_ones(n):
    """Returns number of 1s in the digits of all numbers from 1 to
    n.

    >>> total_ones(10) # 1, 10 -> two 1s
    2
    >>> total_ones(15) # 1, 10, 11, 12, 13, 14, 15 -> eight 1s
    8
    >>> total_ones(21)
    13
    """
    if n == 1:
        return 1

    return count_one(n) + total_ones(n - 1)


def count_one(n):
    """Counts the number of 1s in the digits of n"""
    all_but_last, last = n // 10, n % 10

    increment_one = 1 if last == 1 else 0

    if all_but_last == 0:
        return increment_one

    return increment_one + count_one(all_but_last)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
