from collections import Counter
from itertools import takewhile
from random import choices

cards = {}
inverted = {}
errors = Counter()


def add_card():
    print('The card:')
    while (term := input()) in cards:
        print(f'The card "{term}" already exists. Try again:')
    print('The definition of the card:')
    while (definition := input()) in inverted:
        print(f'The definition "{definition}" already exists. Try again:')
    cards[term] = definition
    inverted[definition] = term
    print(f'The pair ("{term}":"{definition}") has been added.')


def remove_card():
    print('Which card?')
    if (term := input()) in cards:
        del inverted[cards[term]]
        del cards[term]
        print('The card has been removed.')
    else:
        print(f'Can\'t remove "{term}": there is no such card.')


def load_cards():
    print('File name:')
    try:
        count = 0
        with open(input()) as file:
            for line in file:
                term, definition, error_count = line.rstrip().split(':')
                cards[term] = definition
                inverted[definition] = term
                errors[term] = int(error_count)
                count += 1
        print(f'{count} cards have been loaded.')
    except FileNotFoundError:
        print('File not found.')


def save_cards():
    print('File name:')
    with open(input(), 'w') as file:
        for term, definition in cards.items():
            file.write(f'{term}:{definition}:{errors[term]}\n')
    print(f'{len(cards)} cards have been saved.')


def quiz():
    print('How many times to ask?')
    quiz_cards = choices(list(cards.items()), k=int(input()))
    for term, definition in quiz_cards:
        print(f'Print the definition of "{term}":')
        if (answer := input()) == definition:
            print('Correct!')
        else:
            errors[term] += 1
            print(
                f'Wrong. The right answer is "{definition}", but your definition is correct for "{inverted[answer]}".'
                if answer in inverted
                else f'Wrong. The right answer is "{definition}".'
            )


def save_log():
    print('File name:')
    input()
    print('The log has been saved.')


def display_hardest():
    sorted_errors = errors.most_common()
    if not sorted_errors or sorted_errors[0][1] == 0:
        print('There are no cards with errors.')
    else:
        max_errors = sorted_errors[0][1]
        hardest = [pair[0] for pair in takewhile(lambda p: p[1] == max_errors, sorted_errors)]
        print(
            f'The hardest card is {hardest[0]}. You have {max_errors} errors answering it.'
            if len(hardest) == 1
            else f'The hardest cards are {", ".join(hardest)}. You have {max_errors} errors answering them.'
        )


def clear_errors():
    errors.clear()
    print('Card statistics have been reset.')


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
        print(
            '\nInput the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):'
        )
        if (selection := input()) == 'exit':
            print('Bye bye!')
            return
        else:
            actions[selection]()


if __name__ == '__main__':
    main()
