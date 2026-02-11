cards = {}
inverted = {}

print('Input the number of cards:')
for i in range(1, int(input()) + 1):
    print(f'The term for card #{i}:')
    while (term := input()) in cards:
        print(f'The term "{term}" already exists. Try again:')
    print(f'The definition for card #{i}:')
    while (definition := input()) in inverted:
        print(f'The definition "{definition}" already exists. Try again:')
    cards[term] = definition
    inverted[definition] = term

for term, definition in cards.items():
    print(f'Print the definition of "{term}":')
    if (answer := input()) == definition:
        print('Correct!')
    elif answer in inverted:
        print(f'Wrong. The right answer is "{definition}", but your definition is correct for "{inverted[answer]}".')
    else:
        print(f'Wrong. The right answer is "{definition}".')
