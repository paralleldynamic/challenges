class Octopus():
    def __init__(self, starting_energy, location):
        self.energy = starting_energy
        self.location = location
        self.has_flashed = False
        self.neighbors = self.find_neighbors()
        self.times_flashed = 0

    def find_neighbors(self):
        x, y = self.location
        neighbors = set()
        x_start = max(0, x - 1)
        x_end = min(9, x + 1) # promised 10x10 grid of octopuses
        y_start = max(0, y - 1)
        y_end = min(9, y + 1)

        for j in range(y_start, y_end + 1):
            for i in range(x_start, x_end + 1):
                neighbors.add((i, j))

        return neighbors - set((x, y))

    def flash(self):
        self.times_flashed += 1
        self.has_flashed = True
        return self.neighbors

    def time_passes(self):
        self.energy += 1
        neighbors = []

        if (not self.has_flashed) and self.energy > 9:
            neighbors = list(self.flash())

        if self.has_flashed:
            self.energy = 0

        return neighbors

    def end_turn(self):
        self.has_flashed = False

    def __repr__(self):
        return f"Octopus<({self.energy}, {self.location})>"

class Cavern():
    def __init__(self, locations):
        self.octopodes = []
        for y in range(len(locations)):
            for x in range(len(locations[0])):
                self.octopodes.append(Octopus(locations[y][x], (x, y)))

    def find_octopus(self, location):
        for i, octopus in enumerate(self.octopodes):
            if octopus.location == location:
                return self.octopodes[i]


    def render_octopodes(self):
        rendered = []

        for x in range(0, len(self.octopodes), 10):
            mapped = [octopus.energy for octopus in self.octopodes[x:x + 10]]
            rendered.append(mapped)

        return rendered

    def time_passes(self):
        for octopus in self.octopodes:
            neighbor_locations = octopus.time_passes()
            if neighbor_locations:
                for location in neighbor_locations:
                    octo = self.find_octopus(location)
                    neighbor_locations.extend(octo.time_passes())

        for octopus in self.octopodes:
            octopus.has_flashed = False

    def total_energy(self):
        return sum(map(lambda x: x.energy, self.octopodes))


    def __repr__(self):
        return f"Cavern<({len(self.octopodes)} octopodes in cavern.)>"


if __name__ == "__main__":
    # from flashing_octopodes import Cavern, Octopus
    initial_states = []

    with open("input.txt", "r") as input:
        for row in input:
            r = list(map(int, list(row.strip())))
            initial_states.append(r)

    cavern = Cavern(initial_states)
    turns = 0
    while cavern.total_energy() > 0:
        turns += 1
        cavern.time_passes()
        if turns == 100:
            total_flashes = sum(map(lambda x: x.times_flashed, cavern.octopodes))
    print(f"Total flashes at turn 100: {total_flashes}")
    print(f"Turn on which all octopodes flash: {turns}")

