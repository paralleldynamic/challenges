input = list(map(str,range(347312,805915)))

def test_rules(n):
    consecutive = False
    for x, y in zip(n, n[1:]):
        if x > y:
            return False
        if x == y:
            consecutive = True
    return consecutive

if __name__ == '__main__':
    passing = list(filter(test_rules, input))
    
    print(len(passing))