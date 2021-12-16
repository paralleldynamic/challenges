from functools import reduce
from operator import mul


def ribbon(l, w, h):
    area = l * w * h
    x, y = sorted((l, w, h))[:2]
    return area + 2 * x + 2 * y


if __name__ == "__main__":
    with open("input.txt", "r") as input:
        present_dimensions = [tuple(int(d) for d in row.strip().split("x")) for row in input ]

    surface_area = lambda l, w, h: 2 * l * w + 2 * w * h + 2 * l * h + reduce(mul, sorted((l, w, h))[:2])
    print(f"Part 1: {sum([surface_area(l, w, h) for l, w, h in present_dimensions])}")
    print(f"Part 2: {sum([ribbon(l, w, h) for l, w, h in present_dimensions])}")
