from itertools import combinations, product
import re

class Cuboid():
    def __init__(self, xmin, xmax, ymin, ymax, zmin, zmax, instruction):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.zmin = zmin
        self.zmax = zmax
        self.type = instruction
        self.sign = -1 if instruction == "off" else 1
        self.length = xmax - xmin + 1
        self.height = ymax - ymin + 1
        self.width = zmax - zmin + 1
        self.volume = self.length * self.width * self.height
        self.coordinates = list(product((xmin, xmax), (ymin, ymax), (zmin, zmax)))

    def within_bounds(self, cube_limit):
        return len(list(filter(lambda x: abs(x) <= cube_limit, (self.xmin, self.xmax, self.ymin, self.ymax, self.zmin, self.zmax)))) == 0

    def intersects(self, other):
        return all([
            self.xmin <= other.xmax,
            self.xmax >= other.xmin,
            self.ymin <= other.ymax,
            self.ymax >= other.ymin,
            self.zmin <= other.zmax,
            self.zmax >= other.zmin,
        ])

    def overlap(self, other):
        overlap_xmin = max(self.xmin, other.xmin)
        overlap_xmax = min(self.xmax, other.xmax)
        overlap_ymin = max(self.ymin, other.ymin)
        overlap_ymax = min(self.ymax, other.ymax)
        overlap_zmin = max(self.zmin, other.zmin)
        overlap_zmax = min(self.zmax, other.zmax)
        sign = self.sign * other.sign
        if self.sign == other.sign:
            sign = -self.sign
        elif self.sign == 1 and other.sign == -1:
            sign = 1
        instruction = "on" if sign == 1 else "off"
        return Cuboid(overlap_xmin, overlap_xmax, overlap_ymin, overlap_ymax, overlap_zmin, overlap_zmax, instruction)

    def __repr__(self):
        return f"Cuboid<({self.coordinates})>"

class CuboidParser():
    p = re.compile("(\w*) x=(-*\d*)..(-*\d*),y=(-*\d*)..(-*\d*),z=(-*\d*)..(-*\d*)")

    def parse(self, input):
        m = CuboidParser.p.match(input)
        i, *coords = m.groups()
        coords = map(int, coords)
        x0, x1, y0, y1, z0, z1 = coords
        xmin, xmax = min(x0, x1), max(x0, x1)
        ymin, ymax = min(y0, y1), max(y0, y1)
        zmin, zmax = min(z0, z1), max(z0, z1)
        return Cuboid(xmin, xmax, ymin, ymax, zmin, zmax, i)

with open("input.txt", "r") as input:
    parser = CuboidParser()
    cuboids = []
    for row in input:
        cuboids.append(parser.parse(row))
    c = combinations(cuboids, r=2)
    processed = []
    for cuboid in cuboids:
        intersections = []
        for c in processed:
            if cuboid.intersects(c):
                intersections.append(cuboid.overlap(c))
        for c in intersections:
            processed.append(c)
        if cuboid.type == "on":
            processed.append(cuboid)

    volume = sum(map(lambda x: x.volume * x.sign, processed))
    print(f"Part 2: {volume}")
