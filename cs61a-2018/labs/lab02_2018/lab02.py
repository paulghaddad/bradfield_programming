"""Lab 2: Lambda Expressions and Higher Order Functions"""

# Lambda Functions

def lambda_curry2(func):
    """
    Returns a Curried version of a two-argument function FUNC.
    >>> from operator import add
    >>> curried_add = lambda_curry2(add)
    >>> add_three = curried_add(3)
    >>> add_three(5)
    8
    """
    # Alternative
    # def g(x):
    #     def h(y):
    #         return func(x, y)
    #     return h
    # return g

    # Lambda version
    return lambda x: lambda y: func(x, y)
