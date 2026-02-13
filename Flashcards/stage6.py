from collections import Counter
from itertools import takewhile
from random import choices

cards = {}
inverted = {}
errors = Counter()
log = []


def _console_in():
    user_input = input()
    log.append(user_input)
    return user_input


def _console_out(string):
    print(string)
    log.append(string)


def add_card():
    _console_out('The card:')
    while (term := input()) in cards:
        _console_out(f'The card "{term}" already exists. Try again:')
    _console_out('The definition of the card:')
    while (definition := input()) in inverted:
        _console_out(f'The definition "{definition}" already exists. Try again:')
    cards[term] = definition
    inverted[definition] = term
    _console_out(f'The pair ("{term}":"{definition}") has been added.')


def remove_card():
    _console_out('Which card?')
    if (term := input()) in cards:
        del inverted[cards[term]]
        del cards[term]
        _console_out('The card has been removed.')
    else:
        _console_out(f'Can\'t remove "{term}": there is no such card.')


def load_cards():
    _console_out('File name:')
    try:
        count = 0
        with open(_console_in()) as file:
            for line in file:
                term, definition, error_count = line.rstrip().split(':')
                cards[term] = definition
                inverted[definition] = term
                errors[term] = int(error_count)
                count += 1
        _console_out(f'{count} cards have been loaded.')
    except FileNotFoundError:
        _console_out('File not found.')


def save_cards():
    _console_out('File name:')
    with open(_console_in(), 'w') as file:
        for term, definition in cards.items():
            file.write(f'{term}:{definition}:{errors[term]}\n')
    _console_out(f'{len(cards)} cards have been saved.')


def quiz():
    _console_out('How many times to ask?')
    quiz_cards = choices(list(cards.items()), k=int(input()))
    for term, definition in quiz_cards:
        _console_out(f'Print the definition of "{term}":')
        if (answer := input()) == definition:
            _console_out('Correct!')
        else:
            errors[term] += 1
            _console_out(
                f'Wrong. The right answer is "{definition}", but your definition is correct for "{inverted[answer]}".'
                if answer in inverted
                else f'Wrong. The right answer is "{definition}".'
            )


def save_log():
    _console_out('File name:')
    with open(_console_in(), 'w') as file:
        for entry in log:
            print(entry, file=file)
    _console_out('The log has been saved.')


def display_hardest():
    sorted_errors = errors.most_common()
    if not sorted_errors or sorted_errors[0][1] == 0:
        _console_out('There are no cards with errors.')
    else:
        max_errors = sorted_errors[0][1]
        hardest = [pair[0] for pair in takewhile(lambda p: p[1] == max_errors, sorted_errors)]
        _console_out(
            f'The hardest card is {hardest[0]}. You have {max_errors} errors answering it.'
            if len(hardest) == 1
            else f'The hardest cards are {", ".join(hardest)}. You have {max_errors} errors answering them.'
        )


def clear_errors():
    errors.clear()
    _console_out('Card statistics have been reset.')


def main():
    actions = {
        'add': add_card,
        'remove': remove_card,
        'import': load_cards,
        'export': save_cards,
        'ask': quiz,
        'log': save_log,
        'hardest card': display_hardest,
        'reset stats': clear_errors,
    }
    while True:
        _console_out(
            '\nInput the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):'
        )
        if (selection := _console_in()) == 'exit':
            print('Bye bye!')
            return
        else:
            actions[selection]()


if __name__ == '__main__':
    main()
