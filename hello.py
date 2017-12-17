def hello(name):
    '''
    >>> hello('daniel')
    'hello daniel'
    '''
    return 'hello %s' % name

import doctest
test = doctest.DocTestSuite()
