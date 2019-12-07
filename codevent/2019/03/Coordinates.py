from functools import reduce

directions = {
    'U': (0, 1),
    'D': (0, -1),
    'R': (1, 0),
    'L': (-1, 0)
}

def walk(path:list, origin:tuple = (0, 0)):
    coordinates = [origin]
    for turn in path:
        d = turn[0]
        steps = int(turn[1:])
        i = 0
        while i < steps:
            coordinates.append( ((directions[d][0] * 1) + coordinates[-1][0] , (directions[d][1] * 1) + coordinates[-1][1]))
            i += 1
    return coordinates

def walk_until(path:list, destination:tuple = (0,0)):
    step = 0
    for step in range(len(path)):
        if path[step] == destination:
            return step
    return False    

def find_intersections(coordinates):
    return reduce(set.intersection, map(set,coordinates))

def closest_intersection(paths):
    coordinates = []

    for path in paths:
        coordinates.append(walk(path))

    manhattan_distance = lambda x: abs(x[0]) + abs(x[1])
    intersections = find_intersections(coordinates)
    intersections.discard((0,0))
    #min([manhattan_distance(i) for i in intersections]))
    return min(intersections, key=manhattan_distance), intersections, coordinates

if __name__ == '__main__':
    from sys import argv
    wires = []

    with open(argv[1], 'r') as f:
        for r in f:
            wires.append(r.strip().split(','))

    mapped = closest_intersection(wires)
    closest, intersections, paths = mapped[0], mapped[1], mapped[2]
    distances = []
    for intersect in intersections:
        steps = []
        for path in paths:
            steps.append(walk_until(path, intersect))
        distances.append(steps)
    print(min(map(sum, distances)))