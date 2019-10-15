def is_ascending(n):
    """Returns True if the digits of N are in ascending order.

    >>> is_ascending(321)
    True
    >>> is_ascending(123)
    False
    >>> is_ascending(4432221)
    True
    >>> is_ascending(5492)
    False
    >>> is_ascending(5420)
    True
    """
    all_but_last, last = n // 10, n % 10

    while all_but_last > 0:
        second_to_last = all_but_last % 10

        if last > second_to_last:
            return False

        all_but_last, last = all_but_last // 10, all_but_last % 10

    return True



if __name__ == "__main__":
    import doctest
    doctest.testmod()
