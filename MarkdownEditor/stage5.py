OUTPUT_FILE = 'output.md'


class MarkdownDocument:
    def __init__(self):
        self.document = ''

    def append_plain_text(self):
        self.document += input('Text: ')

    def append_bold_text(self):
        self._append_surrounded('**')

    def append_italic_text(self):
        self._append_surrounded('*')

    def append_inline_code(self):
        self._append_surrounded('`')

    def _append_surrounded(self, border):
        text = input('Text: ')
        self.document += border + text + border

    def append_header(self):
        while True:
            try:
                level = int(input('Level: '))
                if level < 1 or level > 6:
                    raise ValueError()
                break
            except ValueError:
                print('The level should be within the range of 1 to 6')
        text = input('Text: ')
        self.document += f'{level * "#"} {text}\n'

    def append_link(self):
        label = input('Label: ')
        url = input('URL: ')
        self.document += f'[{label}]({url})'

    def append_list(self, ordered):
        while True:
            try:
                rows = int(input('Number of rows: '))
                if rows < 1:
                    raise ValueError()
                break
            except ValueError:
                print('The number of rows should be greater than zero')
        for i in range(1, rows + 1):
            row = input(f'Row #{i}: ')
            prefix = f'{i}. ' if ordered else '- '
            self.document += prefix + row + '\n'

    def append_new_line(self):
        self.document += '\n'


doc = MarkdownDocument()

formatters = {
    'plain': doc.append_plain_text,
    'bold': doc.append_bold_text,
    'italic': doc.append_italic_text,
    'header': doc.append_header,
    'link': doc.append_link,
    'inline-code': doc.append_inline_code,
    'ordered-list': lambda: doc.append_list(ordered=True),
    'unordered-list': lambda: doc.append_list(ordered=False),
    'new-line': doc.append_new_line,
}


def main():
    while True:
        match selection := input('Choose a formatter: '):
            case _ if selection in formatters:
                formatters[selection]()
                print(doc.document)
            case '!help':
                print('Available formatters:', ' '.join(formatters))
                print('Special commands: !help !done')
            case '!done':
                with open(OUTPUT_FILE, 'w') as output_file:
                    output_file.write(doc.document)
                break
            case _:
                print('Unknown formatting type or command')


if __name__ == '__main__':
    main()
