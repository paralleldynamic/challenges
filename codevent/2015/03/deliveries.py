from collections import defaultdict

MAPPING = {
    "<": (-1, 0),
    ">": (1, 0),
    "^": (0, 1),
    "v": (0, -1)
}

if __name__ == "__main__":
    with open("input.txt", "r") as input:
        directions = list(input.readline().strip())

    deliveries = defaultdict(int)
    santa_deliveries = defaultdict(int)
    robot_deliveries = defaultdict(int)

    x, y = 0, 0
    deliveries[(0, 0)] = 1
    for dir in directions:
        x_adj, y_adj = MAPPING[dir]
        x += x_adj
        y += y_adj
        deliveries[(x, y)] += 1

    santa_deliveries[(0, 0)] = 1
    robot_deliveries[(0, 0)] = 1
    santa_x, santa_y, robot_x, robot_y = [0] * 4
    for i, dir in enumerate(directions):
        x_adj, y_adj = MAPPING[dir]
        # print(f"x_adj = {x_adj}, y_adj = {y_adj}")
        if i % 2 == 0:
            # print(f"Robot is at ({robot_x}. {robot_y})")
            robot_x += x_adj
            robot_y += y_adj
            robot_deliveries[(robot_x, robot_y)] += 1
            # print(f"Robot moves to ({robot_x}. {robot_y})")
        else:
            # print(f"Santa is at ({santa_x}. {santa_y})")
            santa_x += x_adj
            santa_y += y_adj
            santa_deliveries[(santa_x, santa_y)] += 1
            # print(f"Santa moves to ({santa_x}. {santa_y})")
        # sleep(1)

    print(f"Part 1: {len(deliveries)}")
    print(f"Part 2: {len(set(santa_deliveries.keys()) | set(robot_deliveries.keys()))}")
