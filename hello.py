#!/usr/bin/env python3

def hello(name):
    '''
    >>> hello('daniel')
    'hello daniel'
    '''
    return 'hello %s' % name

import doctest
test = doctest.DocTestSuite()

if __name__ == "__main__":
    print(hello('world'))
