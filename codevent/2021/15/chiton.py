import networkx as nx

class InputReader():
    def __init__(self, input_file_path="input.txt"):
        self.ingest_data(input_file_path)
    def ingest_data(self, input_file_path):
        with open(input_file_path, "r") as input:
            self.risk_matrix = []
            for row in input:
                r = [int(risk) for risk in row.strip()]
                self.risk_matrix.append(r)


def find_neighbors(matrix, location, but_not=None):
    max_y = len(matrix)
    max_x = len(matrix[0])
    up = lambda: (0, -1, max, 0)
    down = lambda: (0, 1, min, max_y - 1)
    left = lambda: (-1, 0, max, 0)
    right = lambda: (1, 0, min, max_x - 1)
    directions = set([up, down, left, right])
    dirs = directions
    if type(but_not) != list:
        but_not = [but_not]
    if but_not:
        dirs -= set(but_not)
    x, y = location
    neighbors = set()
    for dir in dirs:
        x_adj, y_adj, fn, lim = dir()
        neighbor_x = fn(x + x_adj, lim)
        neighbor_y = fn(y + y_adj, lim)
        neighbor = (neighbor_x, neighbor_y)
        neighbors.add(neighbor)
    return neighbors - set([location])


def generate_edges(matrix):
    height = len(matrix)
    width = len(matrix[0])
    get_weight = lambda n: matrix[n[1]][n[0]]
    edges = []
    for y in range(height):
        for x in range(width):
            from_cell = (x, y)
            neighbors = find_neighbors(matrix, from_cell)
            for neighbor in neighbors:
                weight = get_weight(neighbor)
                edge = ((x, y), neighbor, weight)
                edges.append(edge)
    return edges


def generate_graph(edges):
    graph = nx.DiGraph()
    for edge in edges:
        from_node, to_node, weight = edge
        graph.add_edge(from_node, to_node, weight=weight)
    return graph

if __name__ == "__main__":
    ir = InputReader("input.txt")
    rm = ir.risk_matrix
    edges = generate_edges(rm)
    graph = generate_graph(edges)
    shortest_path = nx.dijkstra_path(graph, (0, 0), (9, 9))
    risk_getter = lambda m, x, y: m[y][x]
    risks = [risk_getter(rm, x, y) for node in shortest_path for x, y in node]
    print(sum(risks))
