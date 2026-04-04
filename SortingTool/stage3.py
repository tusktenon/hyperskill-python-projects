import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-dataType', default='word')
parser.add_argument('-sortIntegers', action='store_true')


def get_elements(datatype):
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
    return elements


def display_maximum(elements, datatype):
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


def display_sorted(elements):
    print(f'Total numbers: {len(elements)}.')
    elements.sort()
    print('Sorted data:', *elements, sep=' ')


def main():
    args = parser.parse_args()
    if args.sortIntegers:
        display_sorted(get_elements('long'))
    else:
        datatype = args.dataType
        display_maximum(get_elements(datatype), datatype)


if __name__ == '__main__':
    main()
