from collections import namedtuple

Card = namedtuple('Card', ['question', 'answer'])

cards = []


def main_menu():
    while True:
        print('\n1. Add flashcards\n2. Practice flashcards\n3. Exit')
        match selection := input():
            case '1':
                add_cards_menu()
            case '2':
                practice()
            case '3':
                print('\nBye!')
                return
            case _:
                print(selection, 'is not an option')


def add_cards_menu():
    while True:
        print('\n1. Add a new flashcard\n2. Exit')
        match selection := input():
            case '1':
                get_new_card()
            case '2':
                return
            case _:
                print(selection, 'is not an option')


def practice():
    if not cards:
        print('\nThere is no flashcard to practice!')
        return
    for card in cards:
        print('\nQuestion:', card.question)
        while True:
            print('Please press "y" to see the answer or press "n" to skip:', end=' ')
            match selection := input():
                case 'y':
                    print('\nAnswer: ', card.answer)
                    break
                case 'n':
                    break
                case _:
                    print(selection, 'is not an option')


def get_new_card():
    while not (question := input('Question: ').strip()):
        pass
    while not (answer := input('Answer: ').strip()):
        pass
    cards.append(Card(question, answer))


main_menu()
