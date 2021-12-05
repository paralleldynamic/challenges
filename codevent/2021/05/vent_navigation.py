from collections import Counter
from itertools import chain

def generate_all_points(end_points):
    begin, end = end_points
    begin_x, end_x = begin[0], end[0]
    begin_y, end_y = begin[1], end[1]

    # determine if incrementing or decrementing
    x_direction = 1 if begin_x < end_x else -1
    y_direction = 1 if begin_y < end_y else -1

    # generate coordinates
    if begin_x == end_x:
        l = max(begin_y, end_y) - min(begin_y, end_y) + 1
        x_points = [begin_x] * l
    else:
        x_points = range(begin_x, end_x + x_direction, x_direction)

    if begin_y == end_y:
        l = max(begin_x, end_x) - min(begin_x, end_x) + 1
        y_points = [begin_y] * l
    else:
        y_points = range(begin_y, end_y + y_direction, y_direction)
    all_points = list(zip(x_points, y_points))

    return all_points

class InputReader():
    INPUT_PATH = "input.txt"

    def __init__(self, input_path = INPUT_PATH):
        self.input_path = input_path
        self.read_input_file(input_path)

    def read_input_file(self, input_path):
        coordinates = []
        splitter = lambda x: tuple(map(int, x.split(",")))
        with open(input_path, "r") as input:
            for coordinate_row in input:
                c = coordinate_row.split(" -> ")
                coordinates.append(list(map(splitter, c)))
        self.coordinates = coordinates

    def __repr__(self):
        return f"InputReader<({self.input_path})>: {len(self.coordinates)} lines ingested."


if __name__ == "__main__":
    # for round 1, only consider straight lines
    # f = lambda x: x[0][0] == x[1][0] or x[0][1] == x[1][1]

    ir = InputReader()
    # coordinates = filter(f, ir.coordinates)
    coordinates = ir.coordinates
    points = chain.from_iterable(map(generate_all_points, coordinates))
    counts = Counter(points)
    intersects = [v for k, v in counts.items() if v > 1]
    print(len(intersects))

