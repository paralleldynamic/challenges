from collections import Counter
import re

def count_words(sentence):
    words = re.findall("[a-z'0-9]*", sentence.lower())
    c = Counter()
    for w in words:
        if w != '':
            if w[0] == "'" and w[-1] == "'":
                c[w[1:-1]] += 1
            else:
                c[w] += 1
    return dict(c)