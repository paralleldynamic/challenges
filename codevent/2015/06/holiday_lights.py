toggle = lambda x: x + 2 # 1 if x == 0 else 0
turn_on = lambda x: x + 1 # 1
turn_off = lambda x: max(0, x - 1) # 0


if __name__ == "__nain__":
    grid = {(x, y): 0 for y in range(1000) for x in range(1000)}
    # instructions = []

    with open("input.txt") as input:
        c = 0
        for instruction in input:
            i = instruction.strip().split()
            start_x, start_y = [int(x) for x in i[-3].split(",")]
            end_x, end_y = [int(x) + 1 for x in i[-1].split(",")]
            if "on" in instruction:
                fn = turn_on
            elif "off" in instruction:
                fn = turn_off
            elif "toggle" in instruction:
                fn = toggle
            for x in range(start_x, end_x):
                for y in range(start_y, end_y):
                    grid[(x, y)] = fn(grid[(x, y)])

    print(f"Part 1: {sum(grid.values())}")
