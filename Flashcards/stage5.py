from random import choices

cards = {}
inverted = {}


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
                term, definition = line.rstrip().split(':')
                cards[term] = definition
                inverted[definition] = term
                count += 1
        print(f'{count} cards have been loaded.')
    except FileNotFoundError:
        print('File not found.')


def save_cards():
    print('File name:')
    with open(input(), 'w') as file:
        for term, definition in cards.items():
            file.write(f'{term}:{definition}\n')
    print(f'{len(cards)} cards have been saved.')


def quiz():
    print('How many times to ask?')
    quiz_cards = choices(list(cards.items()), k=int(input()))
    for term, definition in quiz_cards:
        print(f'Print the definition of "{term}":')
        if (answer := input()) == definition:
            print('Correct!')
        elif answer in inverted:
            print(f'Wrong. The right answer is "{definition}", but your definition is correct for "{inverted[answer]}".')
        else:
            print(f'Wrong. The right answer is "{definition}".')


def main():
    actions = {
        'add': add_card,
        'remove': remove_card,
        'import': load_cards,
        'export': save_cards,
        'ask': quiz,
    }
    while True:
        print('\nInput the action (add, remove, import, export, ask, exit):')
        if (selection := input()) == 'exit':
            print('Bye bye!')
            return
        else:
            actions[selection]()


if __name__ == '__main__':
    main()
