from functools import reduce

# Operation to return a 
def prod(n:int):
    return reduce(lambda x, y: x * y, n)

class StateMachine:
    def __init__(self, ops:dict = None):
        self.state = []
        self.memory = []
        if ops is None:
            ops = {1: sum,
                2: prod }
        self.ops = ops
        self.address = 0
        self.pointer = 0
        self.noun = 0
        self.verb = 0
    
    class Instruction:
        def __init__(self, instruction:list, address:int = 4):
                self.opcode = instruction[0]
                self.parameters = instruction[1:4]

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

    def compute(self, state):
        def process_instruction(i):
            opcode = i[0]
            parameters = [state[i[1]], state[i[2]]]
            target = i[3]
            op = self.ops[opcode]
            state[target] = op(parameters)

        i, j = 0, 4

        while j < len(state):
            process_instruction(state[i:j])
            i = j
            j += 4
            if state[i] == 99:
                break

if __name__ == '__main__':
    from sys import argv

    data = argv[1]
    SM = StateMachine()
    SM.collect_state(data)
    SM.memory = SM.remember(SM.state)
    
    terminant = int(argv[2]) + 1
    solution = int(argv[3])

    for i in range(terminant):
        for j in range(terminant):
            noun, verb = i, j
            SM.state[1] = noun
            SM.state[2] = verb
            SM.compute(SM.state)
            if SM.state[0] == solution:
                print(100 * noun + verb)
                break
            SM.reset()
        else:
            continue
        break
