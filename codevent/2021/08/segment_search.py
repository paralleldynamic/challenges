def naive_counts(output):
    digit_length_map = {
        2: 1,
        3: 7,
        4: 4,
        7: 8
    }
    helper = lambda x: 1 if digit_length_map.get(len(x), 0) > 0 else 0
    digits = output.split()
    digit_len = map(helper, digits)
    return sum(list(digit_len))

with open("input.txt", "r") as input:
    cumulative_sum = 0
    for row in input:
        output_digits = row.split("|")[1]
        cumulative_sum += naive_counts(output_digits)

# get counts of all letters
# assign char to c (9), e (4), f (6)
# find maps to one, four, seven, eight (known lengths)
# find b: one except c
# find 2: only digit not containing c
# find five: len 5 and contains f and c
# find three: len 5 contains b and contains c
# find g: four except b, c, f
# find zero: len 6 and does not contain g
# find nine: len 6 and does not contain e
# six is the remaining digits (len 6, does not contain b)

from collections import Counter
from itertools import chain

def alphabetize_string(s):
    return "".join(sorted(list(s)))

def create_mapping(coded_input):
    alphabetized = list(map(alphabetize_string, coded_input))
    def get_counts(digits):
        return list(map(list, digits))
    segment_counts = Counter(chain.from_iterable(get_counts(alphabetized)))
    for k, v in segment_counts.items():
        if v == 9:
            c = k
        elif v == 4:
            e = k
        elif v == 6:
            f = k
    one = list(filter(lambda x: len(x) == 2, alphabetized))[0]
    four = list(filter(lambda x: len(x) == 4, alphabetized))[0]
    seven = list(filter(lambda x: len(x) == 3, alphabetized))[0]
    eight = list(filter(lambda x: len(x) == 7, alphabetized))[0]
    b = one.strip(c)
    two = list(filter(lambda x: c not in x, alphabetized))[0]
    five = list(filter(lambda x: len(x) == 5 and c in x and f in x, alphabetized))[0]
    three = list(filter(lambda x: len(x) == 5 and b in x and c in x, alphabetized))[0]
    g = four.strip(f + c + b)
    zero = list(filter(lambda x: len(x) == 6 and g not in x, alphabetized))[0]
    nine = list(filter(lambda x: len(x) == 6 and e not in x, alphabetized))[0]
    six = list(filter(lambda x: len(x) == 6 and b not in x, alphabetized))[0]
    decoded = [
        zero, one, two, three, four,
        five, six, seven, eight, nine
    ]
    mapping = { v: i for i, v in enumerate(decoded) }
    return mapping


def decode_digits(coded_input, mapping):
    alphabetized = list(map(alphabetize_string, coded_input))
    decoded = list(map(lambda x: mapping[x], alphabetized))
    decoded_value = int("".join(map(str, decoded)))
    return decoded_value

with open("input.txt", "r") as input:
    cumulative_sum = 0
    for row in input:
        key, code = row.split("|")
        mapping = create_mapping(key.strip().split())
        decoded_output = decode_digits(code.strip().split(), mapping)
        print(decoded_output)
        cumulative_sum += decoded_output
