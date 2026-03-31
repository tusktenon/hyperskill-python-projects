import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-dataType', default='word')
datatype = parser.parse_args().dataType

elements = []
while True:
    try:
        match datatype:
            case 'long':
                elements += list(map(int, input().split()))
            case 'line':
                elements.append(input())
            case 'word':
                elements += input().split()
    except EOFError:
        break

greatest = max(elements) if datatype == 'long' else min(elements, key=lambda x: (-len(x), x))
count = elements.count(greatest)
percent = 100 * count // len(elements)

match datatype:
    case 'long':
        print(f'Total numbers: {len(elements)}.')
        print(f'The greatest number: {greatest} ({count} time(s), {percent}%).')
    case 'line':
        print(f'Total lines: {len(elements)}.')
        print(f'The longest line:\n{greatest}\n({count} time(s), {percent}%).')
    case 'word':
        print(f'Total words: {len(elements)}.')
        print(f'The longest word: {greatest} ({count} time(s), {percent}%).')
