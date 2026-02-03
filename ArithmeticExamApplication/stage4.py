import random


def get_test_type():
    while True:
        print(
            'Which level do you want? Enter a number:',
            '1 - simple operations with numbers 2-9',
            '2 - integral squares of 11-29',
            sep='\n',
        )
        match input():
            case '1':
                return 'simple'
            case '2':
                return 'square'
            case _:
                print('Incorrect format.')


def get_integral_answer():
    while True:
        try:
            return int(input())
        except ValueError:
            print('Incorrect format.')


def random_simple():
    expression = f'{random.randint(2, 9)} {random.choice(["+", "-", "*"])} {random.randint(2, 9)}'
    print(expression)
    correct = get_integral_answer() == eval(expression)
    print('Right!' if correct else 'Wrong!')
    return correct


def random_square():
    print(number := random.randint(11, 29))
    correct = get_integral_answer() == number * number
    print('Right!' if correct else 'Wrong!')
    return correct


def main():
    simple_test = get_test_type() == 'simple'
    question = random_simple if simple_test else random_square
    mark = sum([question() for _ in range(5)])
    print(f'Your mark is {mark}/5. Would you like to save the result? Enter yes or no.')
    if input().lower() in ('y', 'yes'):
        test_description = (
            'level 1 (simple operations with numbers 2-9)'
            if simple_test
            else 'level 2 (integral squares with numbers 11-29)'
        )
        name = input('What is your name? ')
        with open('results.txt', 'a') as file:
            file.write(f'{name}: {mark}/5 in {test_description}')
        print('The results are saved in "results.txt".')


if __name__ == '__main__':
    main()
