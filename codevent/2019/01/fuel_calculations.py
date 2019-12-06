from functools import reduce

def calculate_fuel(x):
    return x // 3 - 2

def calculate_inclusive(x):
    fuel = x // 3 - 2
    if fuel <= 0:
        return 0
    return fuel + calculate_inclusive(fuel)

if __name__ == '__main__':
    data = []

    with open('input.txt', 'r') as f:
        for row in f:
            data.append(int(row))

    # PART 1
    a = [i for i in data]
    print(reduce(lambda x, y: x + y, map(calculate_fuel, a)))
    
    # PART 2
    a = [i for i in data]
    print(reduce(lambda x, y: x + y, map(calculate_inclusive, a)))    