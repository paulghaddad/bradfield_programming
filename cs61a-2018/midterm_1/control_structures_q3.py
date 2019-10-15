def count_one(n):
    """Counts the number of 1s in the digits of n

    >>> count_one(7007)
    0
    >>> count_one(123)
    1
    >>> count_one(161)
    2
    >>> count_one(1)
    1
    """
    all_but_last, last = n // 10, n % 10

    increment_one = 1 if last == 1 else 0

    if all_but_last == 0:
        return increment_one

    return increment_one + count_one(all_but_last)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
