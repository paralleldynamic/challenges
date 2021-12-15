from collections import Counter, defaultdict


def generate_pairs(polymer_tempalte):
    pairs = list(zip(polymer_tempalte, polymer_tempalte[1:]))
    return pairs


def polymerize(pair, pair_insertion_rules):
    p = "".join(pair)
    insertion_element = pair_insertion_rules[p]
    insertion = (pair[0], insertion_element, pair[-1])
    return insertion


def synthesize_pairs(pairs):
    joiner = lambda x: "".join(x)
    last_element = pairs[-1][-1]
    elements = map(lambda x: x[:-1], pairs)
    polymer = joiner(map(joiner, elements)) + last_element
    return polymer


def generate_polymer(initial_pairs, rules, iterations):
    polymer_pairs = initial_pairs
    for i in range(iterations):
        trips = []
        for pair in polymer_pairs:
            trips.append(polymerize(pair, rules))
        polymer_string = synthesize_pairs(trips)
        polymer_pairs = generate_pairs(polymer_string)
    return polymer_pairs


def memoize_insertions(template, rules, iterations):
    element_counts = Counter(template)
    polymer = Counter(["".join(p) for p in zip(template, template[1:])])
    for _ in range(iterations):
        synthesizing = defaultdict(int)
        for pair in polymer.keys():
            first_element, second_element = pair
            new_element = rules[pair]
            synthesizing[first_element + new_element] += polymer[pair]
            synthesizing[new_element + second_element] += polymer[pair]
            element_counts[new_element] += polymer[pair]
        polymer = synthesizing
    return element_counts

class InputReader():
    def __init__(self, input_file_path="input.txt"):
        self.pair_insertion_rules = {}
        self.ingest_data(input_file_path)

    def ingest_data(self, input_file_path):
        with open(input_file_path, "r") as input:
            self.polymer_template = input.readline().strip()
            # _ = input.readline() # blank line to separate template from rules
            for rule in input:
                if rule.strip():
                    pair, insertion = rule.strip().split(" -> ")
                    self.pair_insertion_rules[pair] = insertion
            self.initial_pairs = self.generate_pairs(self.polymer_template)

    def generate_pairs(self, polymer_tempalte):
        pairs = list(zip(polymer_tempalte, polymer_tempalte[1:]))
        return pairs

    def polymerize(self, pair):
        p = self._join(pair)
        insertion_element = self.pair_insertion_rules[p]
        insertion = (pair[0], insertion_element, pair[-1])
        return insertion

    def _join(self, elements):
        return "".join(elements)

if __name__ == "__main__":
    ir = InputReader()
    ip = ir.initial_pairs
    rules = ir.pair_insertion_rules
    polymer_pairs = generate_polymer(ip, rules, 40)
    polymer = synthesize_pairs(polymer_pairs)
    c = Counter(polymer)
    print(max(c.values()) - min(c.values()))
