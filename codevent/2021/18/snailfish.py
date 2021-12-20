from dataclasses import dataclass
from functools import reduce
from itertools import permutations

@dataclass()
class NumberWithDepth():
    value: int
    depth: int

    def increment_depth(self):
        return NumberWithDepth(self.value, self.depth + 1)

    def decrement_depth(self):
        return NumberWithDepth(self.value, self.depth - 1)

    def split(self):
        return [
            NumberWithDepth(self.value // 2, self.depth + 1),
            NumberWithDepth(self.value - (self.value // 2), self.depth + 1)
        ]

@dataclass()
class SnailfishNumber():
    numbers: list[NumberWithDepth]

    def __add__(self, other):
        sfn = SnailfishNumber([n.increment_depth() for n in self.numbers + other.numbers])
        sfn.reduce()
        return sfn

    def reduce(self):
        while True:
            l = len(self.numbers)
            self.explode()
            if l != len(self.numbers):
                continue

            self.split()
            if l != len(self.numbers):
                continue
            break

    def explode(self):
        explode_candidates = [i for i, nwd in enumerate(self.numbers) if nwd.depth > 4]
        if len(explode_candidates) > 0:
            index = explode_candidates[0]
            left, right = self.numbers[index:index + 2]
            self.numbers = self.numbers[:index] + [NumberWithDepth(0, left.depth - 1)] + self.numbers[index + 2:]
            self.add(index - 1, left.value)
            self.add(index + 1, right.value)

    def add(self, index: int, num: int):
        if 0 <= index < len(self.numbers):
            self.numbers[index].value += num

    def split(self):
        split_candidates = [(i, nwd) for i, nwd in enumerate(self.numbers) if nwd.value > 9]
        if len(split_candidates) > 0:
            index, to_split = split_candidates[0]
            self.numbers = self.numbers[:index] + to_split.split() + self.numbers[index + 1:]

    def magnitude(self):
        if len(self.numbers) == 1 and self.numbers[0].depth == 0:
            return self.numbers[0].value
        else:
            left, right = self.get_pair()
            return 3 * left.magnitude() + 2 * right.magnitude()

    def get_pair(self):
        halfway = self.halfway()
        numbers = [nwd.decrement_depth() for nwd in self.numbers]
        return SnailfishNumber(numbers[:halfway]), SnailfishNumber(numbers[halfway:])

    def halfway(self):
        percentage_complete = [sum(pow(2, -nums.depth) for nums in self.numbers[:i]) for i in range(len(self.numbers))]
        return percentage_complete.index(0.5)

def parse(s: str):
    nums = []
    depth = 0
    for idx, char in enumerate(s):
        if char == "[":
            depth += 1
        elif char == "]":
            depth -= 1
        elif char.isnumeric():
            nums.append(NumberWithDepth(int(char), depth))

    return SnailfishNumber(nums)

if __name__ == "__main__":
    snailfish_numbers = []
    with open("input.txt", "r") as input:
        for r in input:
            snailfish_numbers.append(parse(r))

    result = reduce(lambda x, y: x + y, snailfish_numbers)
    print(f"Part 1: {result.magnitude()}")
    print(f"Part 2: {max((x + y).magnitude() for x, y in permutations(snailfish_numbers, 2))}")
