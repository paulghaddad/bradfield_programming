def increment(x):
    return x + 1


def square(x):
    return x * x


def make_zipper(f1, f2, sequence):
    """
    Return a function of f1 and f2 composed based on sequence.
    >>> do_nothing = make_zipper(increment, square, 0)
    >>> do_nothing(2)
    2

    >>> incincsq = make_zipper(increment, square, 2)
    >>> incincsq(2)
    4

    >>> sqincinc = make_zipper(increment, square, 1)
    >>> sqincinc(2)
    3

    >>> incincsq = make_zipper(increment, square, 112)
    >>> incincsq(2) # increment(increment(square(2))), so 2 → 4 → 5 → 6
    6
    """
    all_but_last, last = sequence // 10, sequence % 10

    helper = lambda outer, inner: lambda x: outer(inner(x))

    zipper = lambda x: x

    while last:
        if last == 1:
            zipper = helper(f1, zipper)
        else:
            zipper = helper(f2, zipper)

        all_but_last, last = all_but_last // 10, all_but_last % 10

    return zipper


if __name__ == "__main__":
    import doctest
    doctest.testmod()
