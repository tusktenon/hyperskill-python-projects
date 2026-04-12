import argparse
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument('-dataType', default='word')
parser.add_argument('-sortingType', default='natural')


def get_elements(data_type):
    elements = []
    while True:
        try:
            match data_type:
                case 'long':
                    elements += list(map(int, input().split()))
                case 'line':
                    elements.append(input())
                case 'word':
                    elements += input().split()
        except EOFError:
            break
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
    args = parser.parse_args()
    display_sorted(get_elements(args.dataType), args.dataType, args.sortingType)


if __name__ == '__main__':
    main()
