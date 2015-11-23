def hello(name = 'keisatou'):
    """say hello to name

    :param str name: name of person to say hello to. Default is "keisatou".
    :return: None
    :rtype: None

    For example:

    >>> import sphinx_test.app
    >>> sphinx_test.app.hello()
    hello, keisatou!
    >>> sphinx_test.app.hello('world')
    hello, world!
    """
    print("hello, {0}!".format(name))

if __name__ == '__main__':
    hello()
    hello('world')
