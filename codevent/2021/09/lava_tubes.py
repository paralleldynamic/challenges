from itertools import chain
from functools import reduce

with open("input.txt", "r") as input:
    floor_map = []
    for line in input:
        heights = list(line.strip())
        locations = list(map(int, heights))
        floor_map.append(locations)

floor_height = len(floor_map)
max_y = floor_height - 1
floor_width = len(floor_map[0])
max_x = floor_width - 1

low_points = []

def find_neighbors(x, y, max_x, max_y):
    prev_x = max(0, x - 1)
    prev_y = max(0, y - 1)
    next_x = min(max_x, x + 1)
    next_y = min(max_y, y + 1)
    neighbors = [
        (prev_x, y),
        (next_x, y),
        (x, prev_y),
        (x, next_y)
    ]
    return list(set(neighbors) - set([(x, y)]))

def check_points(x, y, points, floor_map):
    current = floor_map[y][x]
    helper = lambda point: floor_map[point[1]][point[0]]
    lowest_neighbor_height = min(map(helper, points))
    if current < lowest_neighbor_height:
        return True, current
    return False, current

for y in range(floor_height):
    for x in range(floor_width):
        points_to_check = find_neighbors(x, y, max_x, max_y)
        low_point, height = check_points(x, y, points_to_check, floor_map)
        if low_point:
            # low_points.append(height) # part 1
            low_points.append((x, y))

# print(sum(low_points) + len(low_points)) # part 1

def map_basin(origin, floor_map, history):
    x, y = origin
    helper = lambda point: floor_map[point[1]][point[0]]
    neighbors = find_neighbors(x, y, max_x, max_y)
    neighbors_filtered = set(filter(lambda x: helper(x) != 9 and x not in history, neighbors)) # - history
    history = history | neighbors_filtered | set([origin])
    if neighbors_filtered:
        for origin in neighbors_filtered:
            for coord in map_basin(origin, floor_map, history):
                history.add(coord)
    return history

basins = [map_basin(origin, floor_map, set()) for origin in low_points]
lens = sorted(map(len, basins), reverse=True)
largest_basins_product = reduce(lambda x, y: x * y, lens[:3])
