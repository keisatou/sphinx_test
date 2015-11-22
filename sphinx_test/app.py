def hello(name = 'keisatou'):
    """say hello to name

    :param str name: name of person to say hello to. Default is "keisatou".
    :return: None
    :rtype: None
    """
    print("hello, {0}!".format(name))

if __name__ == '__main__':
    hello()
    hello('world')
