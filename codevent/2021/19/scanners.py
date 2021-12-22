from collections import Counter, defaultdict
from functools import cache
from itertools import combinations, permutations, product

import numpy as np

TRANSFORMS = list(map(lambda x: np.array(x), product([1, -1], repeat=3)))


def find_offset(first, second):
    diffs = [x * tx - y * ty
        for x, y in list(product(*[first.beacon_arrays(), second.beacon_arrays()]))
        for tx in TRANSFORMS
        for ty in TRANSFORMS
    ]
    counts = Counter(map(tuple, diffs))
    offset, count = counts.most_common()[0]
    print(sorted(set(counts.values()), reverse=True))
    return offset, count


class Scanner():
    def __init__(self, id, beacons):
        self.id = int(id.strip("--- scanner ").strip("---"))
        self.beacons = beacons
        self.calculate_distances()

    def calculate_distances(self):
        def calculate(first, second):
            x1, y1, z1 = first
            x2, y2, z2 = second
            distance = ((x1 - x2)**2 + (y1 - y2)**2 + (z1 - z2)**2)**(1/2)
            return int(distance)

        c = permutations(self.beacons, r=2)
        distances = defaultdict(set)

        for first, second in c:
            d = calculate(first, second)
            distances[first].add((second, d))

        self.distances = distances

    def beacon_array(self):
        return [np.array(b) for b in self.beacons]

    def flattened_distances(self, beacon):
        return [
            (beacon, other, distance)
            for other, distance in self.distances[beacon]
        ]

    @cache
    def beacon_distances(self, beacon):
        return set([
            d for _, d in self.distances[beacon]
        ])

    def __repr__(self):
        return f"Scanner<({self.id})>"



with open("test_input.txt", "r") as input:
    data = input.read().split("\n\n")
    scanners = []
    helper = lambda b: tuple([int(x) for x in b.strip().split(",")])
    for scanner in data:
        id, *beacons = scanner.split("\n")
        b = list(map(helper, filter(lambda x: x, beacons)))
        s = Scanner(id, b)
        scanners.append(s)




# diffs = {}
# for first, second in combinations(scanners, r=2):
#     catch = []
#     for b1 in first.beacons:
#         for b2 in second.beacons:
#             d1 = first.beacon_distances(b1)
#             d2 = second.beacon_distances(b2)
#             if len(d1 & d2) >= 12:
#                 catch.append((b1, b2))
#                 r1 = first.flattened_distances(b1)
#                 r2 = second.flattened_distances(b2)
#                 for _, o1, rd1 in r1:
#                     for _, o2, rd2 in r2:
#                         if rd1 == rd2:
#                             # o1 = np.array(o1)
#                             # o2 = np.array(o2)
#                             catch.append((o1, o2))
#     k = (first.id, second.id)
#     diffs[k] = catch



# for first, second in combinations(scanners, r=2):
#     print(first, second, find_offset(first, second))
