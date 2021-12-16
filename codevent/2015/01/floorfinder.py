from collections import Counter

if __name__ == "__main__":
    with open("input.txt", "r") as input:
        dirs = input.readline().strip()
    c = Counter(dirs)
    print(f"Part 1: {c['('] - c[')']}")

    floor = 0
    for i, bracket in enumerate(dirs):
        floor += 1 if bracket == "(" else -1
        if floor < 0:
            break

    print(f"Part 2: Santa enters the basement at instruction {i + 1}.")


