import argparse
from collections import Counter

parser = argparse.ArgumentParser()
parser.add_argument('-dataType', nargs='?', default='word')
parser.add_argument('-sortingType', nargs='?', default='natural')
parser.add_argument('-inputFile')
parser.add_argument('-outputFile')


def get_elements(data_type, input_file):
    elements = []
    skipped = []

    if input_file:
        with open(input_file) as src:
            for line in src:
                _process_line(line, elements, skipped, data_type)
    else:
        while True:
            try:
                _process_line(input(), elements, skipped, data_type)
            except EOFError:
                break

    for word in skipped:
        print(f'"{word}" is not a long. It will be skipped.')
    return elements


def _process_line(line, elements, skipped, data_type):
    match data_type:
        case 'long':
            for word in line.split():
                try:
                    elements.append(int(word))
                except ValueError:
                    skipped.append(word)
        case 'line':
            elements.append(line)
        case 'word':
            elements += line.split()


def display_sorted(elements, data_type, sort_type, output_file):
    dst = open(output_file, 'w') if output_file else None
    display_name = {'line': 'lines', 'long': 'numbers', 'word': 'words'}[data_type]
    print(f'Total {display_name}: {len(elements)}.', file=dst)
    if sort_type == 'natural':
        elements.sort()
        print('Sorted data:', *elements, sep='\n' if data_type == 'line' else ' ', file=dst)
    else:
        counts = list(Counter(elements).items())
        counts.sort(key=lambda item: (item[1], item[0]))
        for element, count in counts:
            print(f'{element}: {count} time(s), {100 * count // len(elements)}%', file=dst)
    if dst:
        dst.close()


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
    elements = get_elements(args.dataType, args.inputFile)
    display_sorted(elements, args.dataType, args.sortingType, args.outputFile)


if __name__ == '__main__':
    main()
