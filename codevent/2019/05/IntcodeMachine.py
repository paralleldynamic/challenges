from functools import reduce

def prod(n:list):
    '''
    Returns the product of a list of numerics
    '''
    return reduce(lambda x, y: x * y, n)

class IntcodeMachine:
    def __init__(self, ops:dict = None):
        super().__init__()
        self.state = []
        self.memory = []
        if ops is None:
            ops = {1: (sum, 3),
                2: (prod, 3),
                3: (save, 1),
                4: (output, 1) }
        self.ops = ops
        self.address = 0
        self.pointer = 0
        self.noun = 0
        self.verb = 0

    class Instruction():
        super().__init__()
        self.opcode = {}



    def collect_state(self, filename:str):
        '''
        Reads a file containing state into the object's state list

        Anticipates a file with each line being a comma-separated list of integers
        '''
        with open(filename, 'r') as f:
            for r in f:
                for i in r.split(','):
                    self.state.append(int(i))

    def remember(self, state:list):
        return [i for i in state]

    def reset(self):
        del self.state[:]
        for i in self.memory:
            self.state.append(i)

    def save(self, input):

        return
    
    def output(self, input):
        return

    def compute(self):
        state = self.state
        def process_instruction(i):
            opcode = i[0]
            parameters = [state[i[1]], state[i[2]]]
            target = i[3]
            op = self.ops[opcode]
            state[target] = op(parameters)
            return len(i)

        i, j = 0, 4

        while j < len(state):
            address_increment = process_instruction(state[i:j])
            i = j
            j += address_increment
            if state[i] == 99:
                break