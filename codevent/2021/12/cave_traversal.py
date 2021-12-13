class Cave():
    def __init__(self, name):
        self.name = name
        self.dead_end = False
        if name.lower() == name:
            self.visits_limited = True
        else:
            self.visits_limited = False
        self.connections = []
    def create_edge(self, destination):
        self.connections.append(destination)
    def __repr__(self):
        return self.name

class System():
    def __init__(self):
        self.caves = []
        self.routes = []
    def find_cave(self, name):
        c = None
        for i, cave in enumerate(self.caves):
            if cave.name == name:
                c = self.caves[i]
        if not c:
            self.caves.append(Cave(name))
            c = self.caves[-1]
        return c
    def generate_caves_and_edges(self, input_file_path="input.txt"):
        with open (input_file_path, "r") as input:
            for edge in input:
                e = edge.strip().split("-")
                first = self.find_cave(e[0])
                second = self.find_cave(e[1])
                first.create_edge(second)
                second.create_edge(first)
    def mark_dead_ends(self):
        for cave in self.caves:
            if cave.visits_limited and len(cave.connections) == 1 and cave.name not in ["start", "end"]:
                cave.dead_end = True
    def map_route(self, starting_point="end", visited=[]):
        current = self.find_cave(starting_point)
        visited.append(current)
        for edge in current.connections:
            c = self.find_cave(edge.name)
            if (c.visits_limited and c in visited) or c.dead_end:
                return visited
            else:
                return visited + self.map_route(edge.name, visited)


system = System()
system.generate_caves_and_edges("test_input_0.txt")
system.mark_dead_ends()
system.routes.extend(system.map_route("end"))
