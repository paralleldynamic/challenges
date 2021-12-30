from collections import Counter, defaultdict
from functools import cache
from itertools import combinations, permutations, product

import numpy as np

from pprint import pprint

ROTATIONS = sorted(map(lambda x: np.array(x), product([1, -1], repeat=3)), key= lambda x: (sum(x), x[0] ), reverse=True)
ORIENTATIONS = [
    lambda x: np.array((x[0], x[1], x[2])),
    lambda x: np.array((x[0], x[2], x[1])),
    lambda x: np.array((x[1], x[0], x[2])),
    lambda x: np.array((x[1], x[2], x[0])),
    lambda x: np.array((x[2], x[0], x[1])),
    lambda x: np.array((x[2], x[1], x[0])),
]


def find_offset_and_rotation(first, second):
    b0 = first.beacons
    for rotation in ROTATIONS:
        for orientation in ORIENTATIONS:
            b1 = map(orientation, second.rotate_beacons(rotation))
            transformed = [tuple(a - b) for a, b in product(b0, b1)]
            c = Counter(
                transformed
            )
            offset, offset_count = c.most_common()[0]
            if offset_count >= 12:
                return [True, first.id, second.id, offset, rotation, orientation]
    return [False, first.id, second.id, None, rotation, orientation]


class Scanner():
    def __init__(self, name, beacons):
        if type(name) == str:
            self.name = int(name.strip("--- scanner ").strip("---"))
        elif type(name) == int:
            self.name = name
        self.id = hash(
                tuple(beacons)
        )
        self.beacons = np.array([beacon for beacon in beacons])
        self.offset = np.array([0, 0, 0])
        self.rotation = np.array([1, 1, 1])
        self.orientation = ORIENTATIONS[0]

    def rotate_beacons(self, rotations=None):
        if rotations is None:
            rotations = self.rotation
        return self.beacons * rotations

    def orient_beacons(self, orientation=None):
        if orientation is None:
            orientation = self.orientation
        return list(map(orientation, self.beacons))

    def __add__(self, other):
        overlap, _, _, offset, rotation, orientation = find_offset_and_rotation(self, other)
        if not overlap:
            raise ValueError()
            # return [self, other]
        else:
            b0 = set(map(tuple, self.beacons))
            b1 = set(map(tuple, offset + np.array(list(map(orientation, other.beacons * rotation)))))
            b = b0 | b1
            s = Scanner(self.name, b)
            # return [s]
            return s, offset

    def __repr__(self):
        return f"Scanner<({self.name})>"

# class Grid():
#     def append_beacons(self, scanner):
#         # b = set(scanner.rotate_beacons().orient_beacon()
#         # beacons = scanner.offset - b
#         for transformation in scanner.transformations:
#             beacons, offset = transformation.align_beacons(scanner.beacons)
#         self.beacons = self.beacons & set(map(tuple, offset - beacons))
#         return self.beacons


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        data = input.read().split("\n\n")
        scanners = []
        helper = lambda b: tuple([int(x) for x in b.strip().split(",")])
        for scanner in data:
            id, *beacons = scanner.split("\n")
            b = list(map(helper, filter(lambda x: x, beacons)))
            s = Scanner(id, b)
            scanners.append(s)

    grid = scanners
    scanner_coordinates = set()

    while len(grid) != 1:
        placeholder = []
        catch = []
        a = grid[0]
        for i in range(1, len(grid)):
            b = grid[i]
            try:
                s, scanner_coord = a + b
                placeholder.append(s)
                scanner_coordinates.add(scanner_coord)
            except ValueError:
                catch.append(b)
                pass
        grid = placeholder + catch

    manhattan_distances = []

    for first, second in combinations(scanner_coordinates, r=2):
        x0, y0, z0 = first
        x1, y1, z1 = second
        manhattan_distance = sum([abs(x0 - x1), abs(y0 - y1), abs(z0 - z1)])
        manhattan_distances.append(manhattan_distance)

    print(f"Part 1: {len(grid[0].beacons)}")
    print(f"Part 2: {max(manhattan_distances)}")
