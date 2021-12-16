import re


def test_vowels(s):
    re.IGNORECASE
    pattern = "[aeiou]"
    p = re.compile(pattern)
    m = re.findall(p, s)
    if len(m) >= 3:
        return True
    return False


def test_double(s):
    for x, y in zip(s, s[1:]):
        if x == y:
            return True
    return False


def test_forbidden(s):
    for ss in ["ab", "cd", "pq", "xy"]:
        if ss in s:
            return False
    return True


def test_two_pairs(s):
    j = lambda x: "".join(x)
    pairs = map(j, zip(s, s[1:]))
    for pair in pairs:
        if s.count(pair) > 1:
            return True
    return False


def test_sandwich(s):
    trips = zip(s, s[1:], s[2:])
    for x, y, z in trips:
        if x == z:
            return True
    return False


PART_ONE_TESTS = [
    test_vowels,
    test_double,
    test_forbidden
]

PART_TWO_TESTS = [
    test_two_pairs,
    test_sandwich
]

if __name__ == "__main__":
    nice_count = 0
    words = []
    with open("input.txt", "r") as input:
        for line in input:
            s = line.strip()
            words.append(s)

    for s in words:
        nice = True
        for test in PART_ONE_TESTS:
            if not test(s):
                nice = False
        if nice:
            nice_count += 1

    print(f"Part 1: {nice_count} nice words")

    nice_count = 0
    for w in words:
        nice = True
        for test in PART_TWO_TESTS:
            if not test(w):
                nice = False
        if nice:
            nice_count += 1

    print(f"Part 2: {nice_count} nice words")
