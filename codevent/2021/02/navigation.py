INPUT_DATA = "input.txt"

horizontal, vertical = 0, 0

with open(INPUT_DATA, "r") as directions:
    for movement in directions:
        direction, distance = movement.split(" ")
        distance = int(distance)
        if direction == "forward":
            horizontal += distance
        if direction == "down":
            vertical += distance
        if direction == "up":
            vertical -= distance

print(horizontal * vertical)

## part 2
horizontal, depth, aim = 0, 0, 0

with open(INPUT_DATA, "r") as directions:
    for movement in directions:
        direction, distance = movement.split(" ")
        distance = int(distance)
        if direction == "forward":
            horizontal += distance
            depth += distance *  aim
        if direction == "down":
            aim += distance
        if direction == "up":
            aim -= distance
