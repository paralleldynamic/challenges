import re

def abbreviate(words):
    w = re.sub(r'[^A-Z0-9 \']', ' ', words.upper()).split()
    a = ''.join([c[0] for c in w])
    return a
