from functools import reduce

def prod(n:list):
    '''
    Returns the product of a list of numerics
    '''
    return reduce(lambda x, y: x * y, n)

class IntcodeMachine():
    def __init__(self):
        