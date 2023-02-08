from collections import defaultdict

class InputReader():
    def __init__(self, input_file_path="input.txt"):
        self.instructions = []
        self.wires = defaultdict(int)
        with open(input_file_path, "r") as input:
            for row in input:
                self.instructions.append(row.strip().split(" -> "))

def process_instructions():

