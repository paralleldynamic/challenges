import re

from timeit import default_timer as timer

on = lambda: 1
off = lambda: 0

DISPATCHER = {
    "on": on,
    "off": off,
}

class Cuboid():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.state = 0


class Reactor():
    def __init__(self, size):
        self.cuboids = []
        for x in range(-size, size + 1):
            for y in range(-size, size + 1):
                for z in range(-size, size + 1):
                    self.cuboids.append(
                        Cuboid(x, y, z)
                    )

    def find_cuboids(self, xmin, xmax, ymin, ymax, zmin, zmax):
        f = lambda c: xmin <= c.x <= xmax and ymin <= c.y <= ymax and zmin <= c.z <= zmax
        return filter(f, self.cuboids)

    def toggle_cuboids(self, instruction, xmin, xmax, ymin, ymax, zmin, zmax):
        cuboids = self.find_cuboids(xmin, xmax, ymin, ymax, zmin, zmax)
        for cuboid in cuboids:
            cuboid.state = instruction()

if __name__ == "__main__":
    start = timer()
    with open("test_input.txt", "r") as input:
        size = 50 # Part 1
        # r = Reactor(size) # Part 1
        todo = []
        for row in input:
            p = re.compile("(\w*) x=(-*\d*)..(-*\d*),y=(-*\d*)..(-*\d*),z=(-*\d*)..(-*\d*)")
            m = p.match(row)
            i, *coords = m.groups()
            instruction = DISPATCHER[i]
            coords = map(int, coords)
            x0, x1, y0, y1, z0, z1 = coords
            xmin, xmax = min(x0, x1), max(x0, x1)
            ymin, ymax = min(y0, y1), max(y0, y1)
            zmin, zmax = min(z0, z1), max(z0, z1)
            # if max(abs(xmin), abs(xmax), abs(ymin), abs(ymax), abs(zmin), abs(zmax)) > size: #Part 1
            #     continue
            size = max(abs(xmin), abs(xmax), abs(ymin), abs(ymax), abs(zmin), abs(zmax), size)
            todo.append((instruction, xmin, xmax, ymin, ymax, zmin, zmax))

        r = Reactor(size)

        for instruction, xmin, xmax, ymin, ymax, zmin, zmax in todo:
            r.toggle_cuboids(instruction, xmin, xmax, ymin, ymax, zmin, zmax)

    on_cubes = sum(map(lambda c: c.state, r.cuboids))
    # print(f"Part 1: {on_cubes}")
    print(f"Part 2: {on_cubes}")
    end = timer()
    print(f"Runtime was {end - start} seconds")
