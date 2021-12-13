from collections import defaultdict

class CaveSystem():
    def __init__(self):
        self.caves = defaultdict(list)
        self.paths = list()

    @property
    def path_count(self):
        return len(self.paths)

    def is_small_cave(self, name):
        return name.islower()

    def get_neighbors(self, name):
        return self.caves[name]

    def can_visit_cave(self, name, path):
        f = lambda x: self.is_small_cave(x) and x not in ["start", "end"]
        helper = lambda x: path.count(x)
        # if name in ["start", "end"] and name in path:
        #     return False
        # elif max(map(helper, filter(f, path))) == 2:
        #     return False
        # return True
        if not self.is_small_cave(name):
            return True
        elif max(map(helper, filter(f, path))) <= 2:
            return True
        return False

    def ingest_data(self, input_file_path="input.txt"):
        self.caves = defaultdict(list)
        self.paths = list()
        with open(input_file_path, "r") as input:
            for edge in input:
                first, second = edge.strip().split("-")
                self.caves[first].append(second)
                self.caves[second].append(first)

    def _find_path(self, current="start", end="end", path=None, can_visit_again=True):
        if path is None:
            path = []

        path += [current]

        if current == end:
            return [path]

        paths = []
        for neighbor in self.get_neighbors(current):
            if not self.is_small_cave(neighbor) or neighbor not in path:
            # print(neighbor, path, self.can_visit_cave(neighbor, path))
            # if self.can_visit_cave(neighbor, path):
                continued_paths = self._find_path(neighbor, end, list(path), can_visit_again)
                for p in continued_paths:
                    paths.append(p)
            elif can_visit_again and neighbor not in ["start", "end"]:
                continued_paths = self._find_path(neighbor, end, list(path), False)
                for p in continued_paths:
                    paths.append(p)

        return paths

    def find_paths(self, start="start", end="end"):
        self.paths = self._find_path(start, end)
        return self.path_count
