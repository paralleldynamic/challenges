def convert(n):
    s = []
    if n % 3 == 0:
        s.append('Pling')
    if n % 5 == 0:
        s.append('Plang')
    if n % 7 == 0:
        s.append('Plong')
    if s:
        return ''.join(s)
    return str(n)
