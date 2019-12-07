input = list(map(str,range(347312,805915)))

from itertools import groupby

def rules(n):
    consecutive = False
    for x, y in zip(n, n[1:]):
        if x > y:
            return False
        if x == y:
            consecutive = True
    return consecutive

def truly_consecutive(n):
    groups = []
    for _, g in groupby(n):
        groups.append(list(g))
    if 2 in list(map(len, groups)):
        return True
    return False

if __name__ == '__main__':
    passing = list(filter(rules, input))
    answer = list(filter(truly_consecutive, passing))
    print(len(answer))