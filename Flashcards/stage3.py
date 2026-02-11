from collections import namedtuple

Card = namedtuple('Card', ['term', 'definition'])

cards = []
print('Input the number of cards:')
for i in range(1, int(input()) + 1):
    print(f'The term for card #{i}:')
    term = input()
    print(f'The definition for card #{i}:')
    definition = input()
    cards.append(Card(term, definition))

for card in cards:
    print(f'Print the definition of "{card.term}":')
    if input() == card.definition:
        print('Correct!')
    else:
        print(f'Wrong. The right answer is "{card.definition}".')
