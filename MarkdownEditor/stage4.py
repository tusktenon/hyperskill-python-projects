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
                break
            case _:
                print('Unknown formatting type or command')


if __name__ == '__main__':
    main()
