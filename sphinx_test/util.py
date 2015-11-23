def sum_num(n1, n2):
    """return sum of specified numbers

    Example:

    >>> import sphinx_test.util
    >>> sphinx_test.util.sum_num(1, 10)
    11
    >>> sphinx_test.util.sum_num(-1, 10)
    9
    """
    return n1 + n2;


if __name__ == '__main__':
    sum_num(10, 1)
    sum_num(3, 1)
    sum_num(-3, 1)
