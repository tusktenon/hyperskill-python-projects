import argparse
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument('-dataType', nargs='?', default='word')
parser.add_argument('-sortingType', nargs='?', default='natural')


def get_elements(data_type):
    elements = []
    skipped = []
    while True:
        try:
            match data_type:
                case 'long':
                    for word in input().split():
                        try:
                            elements.append(int(word))
                        except ValueError:
                            skipped.append(word)
                case 'line':
                    elements.append(input())
                case 'word':
                    elements += input().split()
        except EOFError:
            break

    for word in skipped:
        print(f'"{word}" is not a long. It will be skipped.')
    return elements


def display_sorted(elements, data_type, sort_type):
    display_name = {'line': 'lines', 'long': 'numbers', 'word': 'words'}[data_type]
    print(f'Total {display_name}: {len(elements)}.')
    if sort_type == 'natural':
        elements.sort()
        print('Sorted data:', *elements, sep='\n' if data_type == 'line' else ' ')
    else:
        counts = list(Counter(elements).items())
        counts.sort(key=lambda item: (item[1], item[0]))
        for element, count in counts:
            print(f'{element}: {count} time(s), {100 * count // len(elements)}%')


def main():
    args, invalid = parser.parse_known_args()
    for arg in invalid:
        print(f'"{arg}" is not a valid parameter. It will be skipped.')
    if args.dataType is None:
        print('No data type defined!')
        exit(1)
    if args.sortingType is None:
        print('No sorting type defined!')
        exit(1)
    display_sorted(get_elements(args.dataType), args.dataType, args.sortingType)


if __name__ == '__main__':
    main()
