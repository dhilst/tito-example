def hello(name: str) -> str:
    '''
    >>> hello('daniel')
    'hello daniel'
    '''
    return f'hello {name}' 

import doctest
test = doctest.DocTestSuite()
