from pprint import pprint

display_helper = lambda x: "".join(map(str, x)).replace("0", " ").replace("1", "#")
display = lambda x: list(map(display_helper, x))


def rotate_matrix(matrix, right=True, flip=False):
    if flip:
        return list(reversed(matrix))

    elif right:
        step_1 = map(reversed, zip(*matrix))
        step_2 = map(list, step_1)
        return list(step_2)

    else:
        step_1 = map(reversed, matrix)
        step_2 = zip(*step_1)
        return list(map(list, step_2))


def fold(matrix, axis, fold_index):
    if axis == "x":
        m = rotate_matrix(matrix)
    else:
        m = matrix

    x_len = len(m[0])
    first = m[:fold_index]
    second = m[fold_index + 1:]
    second = rotate_matrix(second, flip=True)

    if len(first) != len(second):
        if len(first) > len(second):
            diffs = len(first) - len(second)
            dots = [0] * x_len
            second = [list(dots) for i in range(diffs)] + second
        else:
            diffs = len(second) - len(first)
            dots = [0] * x_len
            first = first + [list(dots) for i in range(diffs)]

    m = list(first)

    for y in range(len(first)):
        for x in range(len(first[y])):
            greatest = max(first[y][x], second[y][x])
            m[y][x] = greatest

    if axis == "x":
        m = rotate_matrix(m, right=False)

    return m


class Paper():
    def __init__(self):
        self.matrix = []

    def ingest_data(self, input_file_path="input.txt"):
        marks = []
        fold_instructions = []
        max_x, max_y = 0, 0
        with open(input_file_path, "r") as input:
            for mark in input:
                r = mark.strip()
                if not r:
                    break
                x, y = map(int, r.split(","))
                marks.append((x, y))
                if x > max_x:
                    max_x = x
                if y > max_y:
                    max_y = y
            for instruction in input:
                axis, index = instruction.strip().strip("fold along ").split("=")
                fold_instructions.append((axis, int(index)))
        self.marks = marks
        self.fold_instructions = fold_instructions
        dots = [0] * (max_x + 1)
        self.matrix = [list(dots) for i in range(max_y + 1)]
        # self.matrix = np.array([list(dots) for i in range(max_y + 1)])
        self.process_marks()

    def process_marks(self):
        for mark in self.marks:
            x, y = mark
            self.matrix[y][x] = 1

    def __repr__(self):
        return f"{self.matrix}"

if __name__ == "__main__":
    p = Paper()
    p.ingest_data()

    folded_paper = p.matrix

    for axis, index in p.fold_instructions:
        folded_paper = fold(folded_paper, axis, index)

    pprint(display(folded_paper))
