import argparse
from collections import Counter


class Sorter:
    def __init__(self, data_type, sort_type, input_file, output_file):
        self.data_type = data_type
        self.sort_type = sort_type
        self.input_file = input_file
        self.output_file = output_file
        self.elements = self._load()
        self.sorted = self._sorted()

    def _load(self):
        elements = []
        skipped = []
        if self.input_file:
            with open(self.input_file) as src:
                for line in src:
                    self._process_line(line, elements, skipped)
        else:
            while True:
                try:
                    self._process_line(input(), elements, skipped)
                except EOFError:
                    break

        for word in skipped:
            print(f'"{word}" is not a long. It will be skipped.')
        return elements

    def _process_line(self, line, elements, skipped):
        match self.data_type:
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

    def _sorted(self):
        if self.sort_type == 'natural':
            return sorted(self.elements)
        else:
            counts = list(Counter(self.elements).items())
            return sorted(counts, key=lambda item: (item[1], item[0]))

    def report(self):
        if self.output_file:
            with open(self.output_file, 'w') as dst:
                self._print_report(dst)
        else:
            self._print_report()

    def _print_report(self, dst=None):
        display_name = {'line': 'lines', 'long': 'numbers', 'word': 'words'}[self.data_type]
        print(f'Total {display_name}: {len(self.elements)}.', file=dst)
        if self.sort_type == 'natural':
            sep = '\n' if self.data_type == 'line' else ' '
            print('Sorted data:', *self.sorted, sep=sep, file=dst)
        else:
            for element, count in self.sorted:
                print(f'{element}: {count} time(s), {100 * count // len(self.elements)}%', file=dst)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-dataType', nargs='?', default='word')
    parser.add_argument('-sortingType', nargs='?', default='natural')
    parser.add_argument('-inputFile')
    parser.add_argument('-outputFile')

    args, invalid = parser.parse_known_args()
    for arg in invalid:
        print(f'"{arg}" is not a valid parameter. It will be skipped.')
    if args.dataType is None:
        print('No data type defined!')
        exit(1)
    if args.sortingType is None:
        print('No sorting type defined!')
        exit(1)

    Sorter(args.dataType, args.sortingType, args.inputFile, args.outputFile).report()


if __name__ == '__main__':
    main()
