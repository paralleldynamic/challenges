input = list(map(str,range(347312,805915)))

def two_digits(n):
    i = 0
    for i in range(len(n)):
        if i == 0:
            continue
        if n[i] == n[i - 1]:
            return True
    return False

def incrementing(n):
    i = 0
    for i in range(len(n)):
        if i == 0:
            continue
        if n[i] < n[i-1]:
            return False
    return True

if __name__ == '__main__':
    for n in input:
        if not (two_digits(n) and incrementing(n)):
            input.remove(n)
    
    print(input)