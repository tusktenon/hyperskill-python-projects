import re
import string
from operator import itemgetter

dataset = 'hyperskill-dataset-119013813.txt'


def highest_frequency(s):
    counter = {}
    for c in s:
        counter[c] = counter.get(c, 0) + 1
    return max(counter.values())


def score(password):
    the_score = len(password)
    categories = [
        string.ascii_lowercase,
        string.ascii_uppercase,
        string.digits,
        re.escape('!@#$%^&*'),
    ]
    for pattern in categories:
        if re.search(pattern, password) is None:
            the_score *= 0.75
    if 0.3 * (hf := highest_frequency(password)) >= len(password):
        the_score -= hf
    return the_score


with open(dataset) as file:
    passwords = file.read().rstrip().split('\n')
    print('Highest-scoring password:', max(passwords, key=score))

    # Optional:
    by_score = sorted([(p, score(p)) for p in passwords], key=itemgetter(1), reverse=True)
    print('\nAll passwords')
    for pair in by_score:
        print(f'{pair[1]:.4f}  {pair[0]}')
