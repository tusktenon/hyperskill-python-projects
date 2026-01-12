FORMATTERS = [
    'plain',
    'bold',
    'italic',
    'header',
    'link',
    'inline-code',
    'ordered-list',
    'unordered-list',
    'new-line',
]

while True:
    match selection := input('Choose a formatter: '):
        case _ if selection in FORMATTERS:
            continue
        case '!help':
            print('Available formatters:', ' '.join(FORMATTERS))
            print('Special commands: !help !done')
        case '!done':
            break
        case _:
            print('Unknown formatting type or command')
