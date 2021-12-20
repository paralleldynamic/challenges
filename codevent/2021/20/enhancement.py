from functools import reduce
from itertools import chain
from operator import add

def embed_image(image):
    x_len = len(image[0]) + 2
    new_image = []
    for pixels in image:
        new_image.append(["0"] + pixels + ["0"])
    new_rows = ["0"] * x_len
    new_image = [new_rows] + new_image + [new_rows]
    return new_image


def enhance_image(image, algorithm, iteration):
    x_max = len(image[0])
    y_max = len(image)
    offsets = [
        (-1, -1), (0, -1), (1, -1),
        (-1, 0), (0, 0), (1, 0),
        (-1, 1), (0, 1), (1, 1)
    ]

    def get_pixel_value(pixel, offset):
        x1, y1 = pixel
        x2, y2 = offset
        new_x = x1 + x2
        new_y = y1 + y2
        if new_x < 0 or new_x >= x_max or new_y < 0 or new_y >= y_max:
            if iteration % 2 == 0:
                return "0"
            else:
                return "1"
        return image[new_y][new_x]

    def convert_binary(b):
        return int(b, 2)

    new_image = []

    for y in range(y_max):
        pixels = []
        for x in range(x_max):
            b = ""
            for offset in offsets:
                b += get_pixel_value((x, y), offset)
            pixel = algorithm[convert_binary(b)]
            pixels.append(pixel)
        new_image.append(pixels)

    return new_image


if __name__ == "__main__":
    with open("input.txt") as input:
        algorithm, image = input.read().replace(".", "0").replace("#", "1").split("\n\n")
        image = list(map(list, image.split()))

        for i in range(100):
            image = embed_image(image)

        for i in range(2):
            image = enhance_image(image, algorithm, i)

        lit_pixels_part_one = reduce(add, map(int, chain.from_iterable(image)))
        print(f"Part 1: {lit_pixels_part_one}")

        for i in range(48):
            image = enhance_image(image, algorithm, i)

        lit_pixels_part_two = reduce(add, map(int, chain.from_iterable(image)))

        print(f"Part 2: {lit_pixels_part_two}")
